meta:
  id: cell
  endian: le
  imports:
    - CellHeader
    - Palette
    - Picture
    - Skip
    - View
params:
  - id: file_offset
    type: u2
  - id: cell_offset
    type: u2
  - id: cell_rec_size
    type: u2
  - id: has_palette
    type: b1
    
seq:
  - id: skip_to_cell
    type: skip
    size: file_offset
  - id: header
    type: cell_header
    # size: cell_rec_size
  - id: skip_to_image
    type: skip
    size: relative_image_offset
  - id: image
    size: header.compression == 0 ? header.width  * header.height : header.image_size
    
instances:
  relative_image_offset:
    value: header.image_offset - sizeof<cell_header> - cell_offset