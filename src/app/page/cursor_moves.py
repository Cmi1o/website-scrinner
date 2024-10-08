import pyautogui as GU

from decorators import create_delay


class Cursor:
    @staticmethod
    @create_delay()
    def accept_cookies(has_taskbar: bool=True) -> None:
        y = GU.size().height * 0.9 if has_taskbar else GU.size().height * 0.925
        
        GU.moveTo(
            x=GU.size().width * 0.35,  # координата 0 находится слева
            y=y  # координата 0 находится сверху
        )
        GU.click()
    
    @staticmethod
    def move_to_top() -> None:
        GU.moveTo(x=GU.size().width // 2, y=0 + 1)
    
    @staticmethod
    @create_delay()
    def remove_automatic_software_banner() -> None:
        GU.moveTo(
            x=GU.size().width - 34, 
            y=GU.size().height * 0.13
        )
        GU.click()


cursor = Cursor()
