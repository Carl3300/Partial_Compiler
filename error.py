class Error:
    def __init__(self, name, line, details) -> None:
        self.error_name = name
        self.error_line = line
        self.error_details = details
    def __repr__(self) -> str:
        return f"{self.error_name}: {self.error_details}\nOn line: {self.error_line}"

class InvalidSyntax(Error):
    def __init__(self, line, details) -> None:
        super().__init__("Invalid Syntax", line, details)

class InvalidSemantics(Error):
    def __init__(self, line, details) -> None:
        super().__init__("Invalid Semantics", line, details)

class InvalidCodeGeneration(Error):
    def __init__(self, line, details) -> None:
        super().__init__("Invalid CodeGeneration", line, details)

class ProgramError(Error):
    def __init__(self, line, details) -> None:
        super().__init__("Program Error", line, details)

class BlankFile():
    def __init__(self) -> None:
        pass
    def __repr__(self) -> str:
        return f"The file is either blank or only has comments"

class IllegalChar(Error):
    def __init__(self, line, details) -> None:
        super().__init__("Illegal Character", line, details)