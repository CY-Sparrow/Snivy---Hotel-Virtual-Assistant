# Project Snivy: EU Compliance & Security Insights

## 1. Architectural Pivot: PII-Based vs. Anonymous Reference Flow
This document outlines the transition of the Snivy Virtual Assistant from a traditional PII-collection model (Name, Email, Phone) to a **Privacy-by-Design** model using unique reference numbers.

### 1.1 Comparison Matrix
| Feature | Legacy Flow (PII) | Proposed Flow (Ref #) |
| :--- | :--- | :--- |
| **Data Collected** | Name, Email, Phone, Complaint | Complaint Text Only |
| **Identity Linkage** | Direct (Personal Identity) | Pseudonymous (Ref ID Only) |
| **GDPR Liability** | High (Processing Sensitive PII) | **Low (Data Minimization)** |
| **User Friction** | High (Required Form Entry) | Low (Immediate Submission) |

---

## 2. EU Regulatory Alignment (GDPR/ENISA)

### 2.1 Data Minimization (Article 5)
By removing the requirement for contact details, Snivy follows the "Privacy by Default" principle. The system only processes the data strictly necessary for the "Hotel Complaint" service.

### 2.2 Risk Mitigation
- **Lower Breach Impact:** In the event of a database compromise, the absence of real names and phone numbers prevents identity theft and targeted phishing against guests.
- **Simplified Subject Rights:** Since data is not structured by "Identity," the complexity of fulfilling "Right to Access" or "Right to Portability" requests is significantly reduced.

---

## 3. Technical Implementation (Mapping to Matthew Baker's Book)

The following concepts from *Secure Web Application Development* by Matthew Baker are critical for this new flow:

### 3.1 Secure ID Generation (Chapter 4: Cryptography)
- **Risk:** Sequential IDs (1, 2, 3...) allow attackers to guess other complaints (Insecure Direct Object Reference - IDOR).
- **Solution:** Use **UUIDs** or cryptographically secure random strings for the reference numbers to ensure they are non-guessable.

### 3.2 IDOR Prevention & Access Control (Chapter 10 & 14)
- **Risk:** A user checking the status of a complaint they didn't submit.
- **Solution:** Tie the Reference ID to the user's **Session ID** (Chapter 7) so that only the original submitter can view the status during their active session.

### 3.3 Rate Limiting & Brute Force Defense (Chapter 5: Service Configuration)
- **Risk:** Automated scripts polling the chatbot to find valid reference numbers.
- **Solution:** Implement rate limiting on the `/check-status` endpoint and hide specific error details (e.g., don't distinguish between "ID not found" and "ID pending").

### 3.4 Input Validation (Chapter 7: Cookies and User Input)
- **Risk:** Users may still type PII or malicious scripts into the "Complaint" text field.
- **Solution:** Rigorous server-side validation and sanitization to prevent **SQL Injection** and **XSS**.

---

## 4. Implementation Recommendations for EU Market

1.  **PII Scrubber:** Implement a basic regex-based filter to redact phone numbers or email addresses accidentally provided by users in the complaint text.
2.  **Human-in-the-Loop:** Ensure the chatbot flow informs the user how they can reach a human if the "Reference Number" status does not resolve their issue (EU AI Act requirement for transparency).
3.  **Data Retention Policy:** Automatically purge complaints and associated reference numbers after a set period (e.g., 90 days) to comply with GDPR storage limitation rules.
