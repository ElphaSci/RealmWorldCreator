meta:
  id: view_cell
  endian: le
  imports:
    - ViewCellHeader
    - Palette
params:
  - id: file_offset
    type: u2
  
instances:
  im_offset:
    value: file_offset + header.image_offset
  header:
    pos: file_offset
    type: view_cell_header
  image:
    pos: file_offset + header.image_offset
    size: header.compression == 0 ? header.width  * header.height : header.image_size