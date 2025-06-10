{
  description = "World Builder for The Realm Online";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    devenv.url = "github:cachix/devenv";
    nix2container.url = "github:nlewo/nix2container";
    nix2container.inputs.nixpkgs.follows = "nixpkgs";
    mk-shell-bin.url = "github:rrbutani/nix-mk-shell-bin";

    nix-alien.url = "github:thiagokokada/nix-alien";
  };

  nixConfig = {
    extra-trusted-public-keys = "devenv.cachix.org-1:w1cLUi8dv3hnoSPGAuibQv+f9TZLr6cv/Hm9XgU50cw=";
    extra-substituters = "https://devenv.cachix.org";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.devenv.flakeModule
      ];

      systems = [ "x86_64-linux" "i686-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];

      perSystem = { config, self', inputs', pkgs, system, ... }: {
        # Per-system attributes can be defined here. The self' and inputs'
        # module parameters provide easy access to attributes of the same
        # system.
          _module.args.pkgs = import inputs.nixpkgs {
            inherit system;
            overlays = [
              inputs.nix-alien.overlays.default
            ];
          };

        devenv.shells.default = {
          name = "world-creator-dev";

          languages.python = {
            enable = true;
            package = pkgs.python310Full;
            poetry = {
              enable = true;
              activate.enable = true;
            };
          };

          imports = [
            # This is just like the imports in devenv.nix.
            # See https://devenv.sh/guides/using-with-flake-parts/#import-a-devenv-module
            # ./devenv-foo.nix
          ];

#          config.languages.python.package.withPackages(ps: with ps; [ tkinter]))

          # https://devenv.sh/reference/options/
            packages = with pkgs; [
              upx
              nix-alien
              antlr
          ];

          enterShell = ''
            pip install -e ../KaitaiSCI >> /dev/null
          '';
        };

      };
      flake = {
        # The usual flake attributes can be defined here, including system-
        # agnostic ones like nixosModule and system-enumerating ones, although
        # those are more easily expressed in perSystem.

      };
    };
}
