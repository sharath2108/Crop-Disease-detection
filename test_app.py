"""
Automated Test & Verification Suite for AgriVision AI
Tests database, user authentication, unique User ID generation,
MobileNetV2 prediction, dataset leaf comparison, fertilizer data, and Flask routing.
"""

import os
import unittest
from app import app
from database import init_db, register_user, authenticate_user, get_user_by_id, save_diagnosis, get_user_diagnoses
from model_loader import predict_crop_disease, get_reference_sample_images
from disease_data import ORDERED_CLASSES, get_disease_profile

class TestCropDiseaseApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    def test_01_classes_and_profiles(self):
        """Verify all 38 PlantVillage classes have valid profiles and fertilizer data"""
        self.assertEqual(len(ORDERED_CLASSES), 38)
        for cls_name in ORDERED_CLASSES:
            prof = get_disease_profile(cls_name)
            self.assertIn("crop", prof)
            self.assertIn("condition", prof)
            self.assertIn("fertilizers", prof)
            self.assertIn("primary_npk", prof["fertilizers"])
            self.assertIn("precautions", prof)
            self.assertGreater(len(prof["precautions"]), 0)

    def test_02_user_registration_and_id(self):
        """Verify user registration generates proper AGRI-USER-XXXXX identifier"""
        import random
        rand_suffix = random.randint(1000, 9999)
        test_username = f"farmer_test_{rand_suffix}"
        test_email = f"farmer_{rand_suffix}@farm.com"
        
        user_id, err = register_user(
            username=test_username,
            full_name="Sharath Test User",
            email=test_email,
            password="securePassword123",
            farm_location="Green Valley",
            crop_interests="Tomato, Potato"
        )
        self.assertIsNone(err)
        self.assertTrue(user_id.startswith("AGRI-USER-"))

        # Verify authentication with User ID
        auth_user = authenticate_user(user_id, "securePassword123")
        self.assertIsNotNone(auth_user)
        self.assertEqual(auth_user["username"], test_username)

        # Verify authentication with Username
        auth_user_2 = authenticate_user(test_username, "securePassword123")
        self.assertIsNotNone(auth_user_2)
        self.assertEqual(auth_user_2["user_id"], user_id)

    def test_03_stored_dataset_reference_samples(self):
        """Verify dataset reference sample retrieval for classes"""
        ref_sample, healthy_sample = get_reference_sample_images("Tomato___Early_blight")
        self.assertIsNotNone(ref_sample)
        self.assertTrue(os.path.exists(os.path.join("static", ref_sample)))

    def test_04_prediction_and_comparison_pipeline(self):
        """Verify MobileNetV2 inference and dataset similarity computation"""
        sample_img = "static/dataset_samples/Tomato___Early_blight"
        files = [os.path.join(sample_img, f) for f in os.listdir(sample_img) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if files:
            res = predict_crop_disease(files[0])
            self.assertIn("predicted_class", res)
            self.assertIn("confidence", res)
            self.assertIn("similarity_score", res)
            self.assertIn("profile", res)
            self.assertGreater(res["similarity_score"], 0)
            self.assertIn("primary_npk", res["profile"]["fertilizers"])
            self.assertGreater(len(res["profile"]["precautions"]), 0)

    def test_05_flask_routes(self):
        """Verify essential web routes respond with HTTP 200/302"""
        tester = app.test_client(self)
        
        # Public auth routes
        resp = tester.get('/login')
        self.assertEqual(resp.status_code, 200)

        resp = tester.get('/register')
        self.assertEqual(resp.status_code, 200)

        # Protected route redirects to login when not authenticated
        resp = tester.get('/dashboard')
        self.assertEqual(resp.status_code, 302)

if __name__ == '__main__':
    unittest.main()
