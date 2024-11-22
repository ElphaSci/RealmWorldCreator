{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... } @ inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python311;
        kaitaisci = pkgs.python311Packages.buildPythonPackage rec {
          pname = "kaitaisci";
          version = "0.1";
          src = builtins.fetchGit {
            ref = "main";
            url = "https://github.com/ElphaSci/KaitaiSci.git";
          };
          propagatedBuildInputs = with pkgs.python311Packages; [
            pillow
            kaitaistruct
          ];

          meta = {
            description = "Python Parser for Sierra Creative Interpreter files, using Kaitai";
            homepage = "https://github.com/ElphaSci/KaitaiSci.git";
            email = "cmhulbert@gmail.com";
          };
        };
      in rec {
        devShells = {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python311 virtualenv
              rustc cargo gcc rustfmt clippy
             ] ++
              (with pkgs.python311Packages; [
                ipython
                pip
                kaitaisci
                matplotlib
                pysimplegui
                cx_Freeze
                venvShellHook
              ]);

            venvDir = ".venv";
            postShellHook = ''
              # Allow the use of wheels.
              unset SOURCE_DATE_EPOCH
              ( IFS=:
                for p in $PYTHONPATH; do
                  ln -s $p/* /home/caleb/git/Realm_World_Creator/.venv/lib/python3.11/site-packages
                done
              )
            '';
            postVenv = ''
              unset SOURCE_DATE_EPOCH
              pip install -e .
            '';
          };
        };
      }
    );
}
