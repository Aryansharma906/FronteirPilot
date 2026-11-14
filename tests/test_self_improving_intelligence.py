import unittest
from pathlib import Path
from lib.self_improving_intelligence import SelfImprovingIntelligenceEngine


class TestSelfImprovingIntelligence(unittest.TestCase):
    def setUp(self):
        self.engine = SelfImprovingIntelligenceEngine()

    def test_load_and_save_calibration(self):
        cal = self.engine.load_calibration()
        self.assertIn("skill_weights", cal)
        self.assertIn("LLM Evaluation", cal["skill_weights"])
        self.assertGreaterEqual(cal["skill_weights"]["LLM Evaluation"], 1.0)

    def test_calibrate_from_outcomes(self):
        test_opps = [
            {"status": "Interviewing", "matching_skills": ["LLM Evaluation", "Python"]},
            {"status": "Offered / Accepted", "matching_skills": ["Prompt Injection"]},
            {"status": "Rejected", "matching_skills": ["Legacy Cobol"]}
        ]
        res = self.engine.calibrate_from_outcomes(test_opps)
        self.assertGreater(res["progressions_analyzed"], 0)
        self.assertIn("cycles_completed", res)

    def test_extract_market_trends(self):
        test_opps = [
            {"matching_skills": ["LLM Evaluation", "Python", "PyTorch"]},
            {"matching_skills": ["LLM Evaluation", "FastAPI", "Docker"]},
            {"matching_skills": ["Autonomous Agents", "Prompt Injection"]}
        ]
        trends = self.engine.extract_market_trends(test_opps)
        self.assertIn("top_market_skills", trends)
        self.assertTrue(len(trends["top_market_skills"]) > 0)
        self.assertIn("verified_matching_strengths", trends)

    def test_evaluate_bullet_quality(self):
        high_quality = "Architected automated evaluation suite benchmarking 5,000+ frontier LLM completions across multi-turn reasoning and safety guardrails, reducing prompt failure rate by 34%."
        res = self.engine.evaluate_bullet_quality(high_quality)
        self.assertTrue(res["has_metrics"])
        self.assertTrue(res["starts_with_strong_verb"])
        self.assertGreaterEqual(res["composite_score"], 85)
        self.assertIn(res["ats_grade"], ("A+", "A"))

        weak_bullet = "Worked on some tasks."
        weak_res = self.engine.evaluate_bullet_quality(weak_bullet)
        self.assertFalse(weak_res["has_metrics"])
        self.assertLess(weak_res["composite_score"], 70)

    def test_run_self_healing_maintenance(self):
        diag = self.engine.run_self_healing_maintenance()
        self.assertIn("integrity_check", diag)
        self.assertEqual(diag["integrity_check"], "ok")

    def test_run_autonomous_intelligence_cycle(self):
        cycle_res = self.engine.run_autonomous_intelligence_cycle()
        self.assertEqual(cycle_res["status"], "self_improvement_cycle_successful")
        self.assertIn("learning_outcomes", cycle_res)
        self.assertIn("market_intelligence", cycle_res)


if __name__ == "__main__":
    unittest.main()
