from gui import AutoClickerGUI
from autoclicker import AutoClicker

if __name__ == "__main__":
    print("Starting AutoClicker...")
    auto_clicker = AutoClicker()
    gui = AutoClickerGUI(auto_clicker)
    gui.run()
