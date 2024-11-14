#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.research_crew.research_crew import ResearchCrew


class ResearchState(BaseModel):
    research_output: str = ""


class ResearchFlow(Flow[ResearchState]):

    @start()
    def initiate_research(self):
        print("Initiating research on unsupervised machine learning developments")
        result = (
            ResearchCrew()
            .crew()
            .kickoff()
        )
        self.state.research_output = result.raw
        print("Research completed", self.state.research_output)


def kickoff():
    research_flow = ResearchFlow()
    research_flow.kickoff()


if __name__ == "__main__":
    kickoff()
