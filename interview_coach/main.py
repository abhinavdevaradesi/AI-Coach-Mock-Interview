from controllers.cli_controller import CLIController

def main():
    """Entry point for the application."""
    controller = CLIController()
    controller.run()

if __name__ == "__main__":
    main()