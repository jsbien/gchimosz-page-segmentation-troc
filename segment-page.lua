--
-- Find segmentation of page
-- (c) Grzegorz Chimosz 2008-2009
-- released under GNU GPL with ABSOLUTELY NO WARRANTY
--

import_all(graphics)
import_all(ocr)
import_all(iulib)

if #arg < 3 or #arg > 4 then
    print(arg[0] .. " - a simple script that finds segmentation and dump it")
    print("Usage: " .. arg[0] .. " <input image> <output image> <output text file> [-c]")
    os.exit(1)
end

-- load an image
input = bytearray()
read_image_gray(input, arg[1])

-- deskew it
deskew = make_DeskewPageByRAST()
deskewed = bytearray()
deskew:cleanup(deskewed, input)

-- binarize it
binarizer = make_BinarizeBySauvola()
binarized = bytearray()
binarizer:binarize(binarized, deskewed)

-- perform layout analysis
segmenter = make_SegmentPageByRAST()
segmentation = intarray()
segmenter:segment(segmentation, binarized)

-- dump the column boxes
regions = RegionExtractor()
regions:setPageLines(segmentation)
output = io.open(arg[3], 'w')
for i = 1, regions:length() - 1 do
    local bbox = regions:bbox(i)

    -- (x0, y0) is the lower left corner;
		-- (x1, y1) is the upper right corner;
		-- (0, 0) is lowest left point of page, just as in DjVu
    output:write(("%d %d %d %d\n"):format(bbox.x0, bbox.y0, (bbox.x1 - bbox.x0), (bbox.y1 - bbox.y0)))
end

-- colorize layout analysis result
-- and write output file
if #arg == 4 and arg[4] == "-c" then
	check_page_segmentation(segmentation)
	simple_recolor(segmentation)

	write_image_packed(arg[2], segmentation)
else
	write_image_gray(arg[2], deskewed)
end

