from PIL import Image
import base64
import io
from typing import Optional, List, Iterable
from openai.types.chat import ChatCompletionContentPartImageParam


def encode_image(image_path: str) -> Optional[str]:
    """Encode an image to base64 string"""
    with Image.open(image_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")


def get_encoding_for_images(image_paths: List[str]) -> Iterable[ChatCompletionContentPartImageParam]:
    """Convert a list of image paths to ChatCompletionContentPartImageParam objects"""
    image_inputs: List[ChatCompletionContentPartImageParam] = [
        ChatCompletionContentPartImageParam(
            type="image_url",
            image_url={
                "url": f"data:image/png;base64,{encode_image(path)}",
                "detail": "high"
            }
        )
        for path in image_paths
    ]
    return image_inputs