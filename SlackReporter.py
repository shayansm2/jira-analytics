from abc import ABC

from ReporterInterface import ReporterInterface


class SlackReporter(ReporterInterface, ABC):
    def send_message(self, message: str):
        pass