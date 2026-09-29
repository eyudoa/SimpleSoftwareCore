# Simple software underlying logic skeleton
# Not a complete application, only demonstrates basic runtime logic
class AppCore:
    def __init__(self):
        self.is_running = True
        self.app_state = "idle"

    def set_state(self, new_state: str):
        self.app_state = new_state

    def handle_input(self, user_input: str):
        match user_input.lower():
            case "quit":
                self.is_running = False
            case "start":
                self.set_state("working")
            case "stop":
                self.set_state("idle")

    def main_loop(self):
        while self.is_running:
            print(f"Current state: {self.app_state}")
            user_input = input("> ")
            self.handle_input(user_input)

# Program entry
if __name__ == "__main__":
    app = AppCore()
    app.main_loop()
