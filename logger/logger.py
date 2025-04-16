import datetime

class Logger:
    def __init__(self, filename="app.log"):
        self.filename = filename

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"[{timestamp}] {level}: {message}"
        print(formatted)

        with open(self.filename, "a") as f:
            f.write(formatted + "\n")

    def info(self, message):
        self._log("INFO", message)

    def warning(self, message):
        self._log("WARNING", message)

    def error(self, message):
        self._log("ERROR", message)

l = Logger()
l.info("Server started")
l.warning("Memory usage high")
l.error("Connection failed")

