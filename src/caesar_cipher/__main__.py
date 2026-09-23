"""Run the Caesar cipher desktop application."""


def main() -> None:
    """Create and run the application."""
    try:
        from .gui import CaesarCipherApp
    except ModuleNotFoundError as error:
        if error.name == "_tkinter":
            raise SystemExit(
                "Tkinter is required to run the desktop app. "
                "Install your system's Tk package and try again."
            ) from None
        raise

    app = CaesarCipherApp()
    app.run()


if __name__ == "__main__":
    main()