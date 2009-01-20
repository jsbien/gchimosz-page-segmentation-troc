-- http://markmail.org/message/5wqdj3avtvacs62m#query:make_SegmentPageByRAST+page:1+mid:cr2qdjla6qzdoxin+state:results

import_all(graphics)
import_all(ocr)
import_all(iulib)

if #arg < 2 then
    print(arg[0].." - a sample script that dumps bounding boxes of columns")
    print("Usage: "..arg[0].." <input image> <output text file>")
    os.exit(1)
end

-- load an image
input = bytearray()
read_image_gray(input,arg[1])

-- binarize it
binarizer = make_BinarizeBySauvola()
binarized = bytearray()
binarizer:binarize(binarized, input)

-- perform layout analysis
segmenter = make_SegmentPageByRAST()
segmentation = intarray()
segmenter:segment(segmentation, binarized)

-- dump the column boxes
regions = RegionExtractor()
-- (ch) regions:setPageColumns(segmentation)
regions:setPageLines(segmentation)
output = io.open(arg[2], 'w')
height = segmentation:dim(1)
for i = 1, regions:length() - 1 do
    local bbox = regions:bbox(i)

    -- flip the y coordinate
    bbox.y0 = height - bbox.y0 - 1
    bbox.y1 = height - bbox.y1 - 1

    -- (x0, y0) is the lower left corner;
    -- we print (x0, y1) (upper left) and (x1, y0) (lower right) corners.
    output:write(("%d %d %d %d\n"):format(bbox.x0, bbox.y1, bbox.x1, bbox.y0))
end
