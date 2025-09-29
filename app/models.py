from pydantic import BaseModel
from typing import List, Dict, Optional

class ImplementationLocation(BaseModel):
    file: str
    function: str
    lines: str

class FeatureAnalysisItem(BaseModel):
    feature_description: str
    implementation_location: List[ImplementationLocation]

class ExecutionPlanSuggestion(BaseModel):
    suggestion: str

class TestResult(BaseModel):
    tests_passed: bool
    log: str

class FunctionalVerification(BaseModel):
    generated_test_code: str
    execution_result: TestResult

class AnalysisReport(BaseModel):
    feature_analysis: List[FeatureAnalysisItem]
    execution_plan_suggestion: str
    functional_verification: Optional[FunctionalVerification] = None