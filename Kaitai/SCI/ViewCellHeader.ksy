meta:
  id: view_cell_header
  endian: le
    
seq:
- id: width
  type: s2
- id: height
  type: s2
- id: x_shift
  type: s2
- id: y_shift
  type: s2
- id: transparent_color
  type: u1
- id: compression
  type: u1
- id: flags
  type: s2
- id: image_and_pack_size
  type: u4
- id: image_size
  type: u4
- id: palette_offset
  type: u4
  doc: "Relative to end of cell header"
- id: image_offset
  type: u4
  doc: "Relative to start of file, after offset"
- id: pack_data_offset
  type: u4
- id: lines_offset
  type: u4
- id: link_table_offset
  type: s4
- id: link_number
  type: s2

instances:
  struct_size:
    value: 42
  
  