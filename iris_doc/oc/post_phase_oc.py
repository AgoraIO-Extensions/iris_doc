import subprocess
from typing import Any

from iris_doc.post_phase import PostPhase

class PostPhaseObjC(PostPhase):

    __executePath: str

    def __init__(self, executePath: str) -> None:
        self.__executePath = executePath

    def run(self) -> Any:
        p = subprocess.Popen(["flutter", "format", "."], cwd=self.__executePath)
        p.wait()