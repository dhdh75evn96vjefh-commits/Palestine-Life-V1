from colorama import init, Fore, Style
init(autoreset=True)

class Colors:
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
    
    @staticmethod
    def success(text):
        return f"{Fore.GREEN}[✓] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def error(text):
        return f"{Fore.RED}[✗] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def warning(text):
        return f"{Fore.YELLOW}[!] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def info(text):
        return f"{Fore.CYAN}[ℹ] {text}{Style.RESET_ALL}"
