import React, { useState } from "react";
import axios from "axios";
import styles from "./PatientForm.module.css";

const fields = [
    "breathing_problem",
    "fever",
    "dry_cough",
    "sore_throat",
    "running_nose",
    "asthma",
    "chronic_lung_disease",
    "headache",
    "heart_disease",
    "diabetes",
    "hyper_tension",
    "fatigue",
    "gastrointestinal",
    "abroad_travel",
    "contact_with_covid_patient",
    "attended_large_gathering",
    "visited_public_exposed_places",
    "family_working_in_public_exposed_places",
];

const PatientForm = () => {
    const [patientData, setPatientData] = useState({});
    const [message, setMessage] = useState("");

    const handleChange = e => {
        setPatientData({
            ...patientData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async e => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/patients/', patientData)
            setMessage(response.data.message);
        } catch (error) {
            setMessage("An error occurred while submitting the form.");
        }
    };

    return (
        <div>
            <header className={styles.header}>
                <h1>COVID-19 Self-Checker Questionnaire</h1>
            </header>
            <div className={styles.formContainer}>
                {/* <h2>Questionnaire</h2> */}
                <form onSubmit={handleSubmit}>
                    {fields.map(field => (
                        <div key={field} className={styles.formField}>
                            <label>{field.replace("_", " ")}</label>
                            <select name={field} onChange={handleChange}>
                                <option value="">Select...</option>
                                <option value="0">No</option>
                                <option value="1">Yes</option>
                            </select>
                        </div>
                    ))}
                    <button type="submit" className={styles.submitButton}>Submit</button>
                </form>
                {message && <p className={styles.message}>{message}</p>}
            </div>
        </div>
    );
};

export default PatientForm;
