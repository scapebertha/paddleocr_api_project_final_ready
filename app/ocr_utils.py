
from paddleocr import PaddleOCR

ocr_arabic_layout = PaddleOCR(use_angle_cls=True, lang='ar', show_log=False)
ocr_arabic_simple = PaddleOCR(use_angle_cls=False, lang='ar', det_db_box_thresh=0.5, show_log=False)
ocr_english = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

def run_ensemble_ocr(image):
    result = {
        'layout_ar': ocr_arabic_layout.ocr(image, cls=True),
        'simple_ar': ocr_arabic_simple.ocr(image, cls=False),
        'english': ocr_english.ocr(image, cls=True)
    }
    return result
