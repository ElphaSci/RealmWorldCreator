meta:
  id: picture_header
  endian: le
seq:
- id: cell_offset
  type: s2
- id: num_cells
  type: s1
- id: is_compressed
  type: b1
- id: cell_rec_size
  type: u2
- id: palette_offset
  type: u2
- id: skip_bytes
  size: 2
- id: width
  type: u2
- id: height
  type: u2
  
