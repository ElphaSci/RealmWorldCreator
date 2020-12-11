meta:
  id: loop_header
  endian: le
  
seq:
  - id: based_on_loop
    type: s1
  - id: mirror
    type: b1le
  - id: num_cells
    type: u1
  - id: unknown_bytes_2
    size: 9
  - id: cells_offset
    type: u4
