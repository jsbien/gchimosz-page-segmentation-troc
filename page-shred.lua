-- (c) Grzegorz Chimosz 2008
-- This script comes with absolutely no warranty under GNU GPL

import_all(graphics)
import_all(ocr)
import_all(iulib)

image = bytearray:new()
read_image_gray(image, arg[1])

corrector = make_DeskewPageByRAST()
clean = bytearray:new()
corrector:cleanup(clean, image)

-- segmenter = make_SegmentPageByRAST() -- mocno szatkuje, niepotrzebnie tnie kolumny
-- segmenter = make_SegmentPageByXYCUTS() -- slabo
segmenter = make_SegmentPageByMorphTrivial() -- nie daje rady dla duble-skanu
-- segmenter = make_SegmentPageByVORONOI() -- slabo
-- segmenter = make_SegmentPageBySmear -- slabo
segmentation = intarray()
segmenter:segment(segmentation, clean)

regions = RegionExtractor()
-- regions:setPageLines(segmentation)
regions:setPageColumns(segmentation)
region = bytearray()
-- recognizer = make_TesseractRecognizeLine()
for i = 1, regions:length() - 1 do
	regions:extract(region, image, i, 1)
	-- fst = make_StandardFst()
	-- recognizer:recognizeLine(fst, region)
	-- s = nustring()
	-- fst:bestpath(s)
	-- print(s:utf8())
	write_image_gray(arg[1] .. "-" .. i .. ".png", region)
end
