meta:
  id: view_header
  endian: le
  
seq:
  - id: loop_table_offset
    type: u2
  - id: num_loops
    type: u1
  - id: unknown_byte
    size: 1 
  - id: compressed
    type: b1le
  - id: view_size
    type: u1
  - id: num_cells
    type: u2
  - id: palette_offset
    type: u4
  - id: loop_rec_size
    type: u1
  - id: cell_rec_size
    type: u1
  - id: x_res
    type: u2
  - id: y_res
    type: u2

instances:
  has_links:
    value: cell_rec_size == 0x034