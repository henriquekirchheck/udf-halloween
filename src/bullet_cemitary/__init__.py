from bullet_cemitary.app import App
from bullet_cemitary.soul import Soul


def main() -> None:
    app = App()
    app.add_children(Soul())
    app.run()


if __name__ == "__main__":
    main()
