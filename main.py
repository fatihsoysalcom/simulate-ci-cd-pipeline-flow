import sys
import time

# --- Configuration for demonstration ---
# Set these flags to True to simulate failures at different stages.
SIMULATE_BUILD_FAILURE = False
SIMULATE_TEST_FAILURE = False
SIMULATE_DEPLOY_STAGING_FAILURE = False
# --- End Configuration ---

def log(message, level="INFO"):
    """Helper function for consistent logging and simulating work."""
    print(f"[{level}] {message}")
    time.sleep(0.5) # Simulate work being done

def build_project():
    """Simulates the build phase of a CI/CD pipeline."""
    log("Starting build phase...")
    if SIMULATE_BUILD_FAILURE:
        log("Build failed! (Simulated)", "ERROR")
        return False
    log("Project built successfully.")
    return True

def run_tests():
    """Simulates the automated testing phase."""
    log("Starting automated testing phase...")
    log("Running unit tests...")
    log("Running integration tests...")
    if SIMULATE_TEST_FAILURE:
        log("Tests failed! (Simulated)", "ERROR")
        return False
    log("All tests passed successfully.")
    return True

def deploy_to_staging():
    """Simulates deployment to a staging environment."""
    log("Starting deployment to staging environment...")
    log("Packaging application...")
    log("Transferring package to staging server...")
    log("Starting application on staging...")
    if SIMULATE_DEPLOY_STAGING_FAILURE:
        log("Deployment to staging failed! (Simulated)", "ERROR")
        return False
    log("Application successfully deployed to staging.")
    return True

def deploy_to_production():
    """Simulates deployment to a production environment."""
    log("Starting deployment to production environment...")
    log("Running pre-deployment checks...")
    log("Transferring package to production servers...")
    log("Updating production database schema (if needed)...")
    log("Switching traffic to new version...")
    log("Post-deployment verification...")
    log("Application successfully deployed to production!")
    return True

def run_ci_cd_pipeline():
    """Orchestrates the simulated CI/CD pipeline."""
    log("--- CI/CD Pipeline Started ---", "PIPELINE")

    # 1. Continuous Integration (CI) part
    log("Fetching latest code from version control (e.g., Git)...") # CI: Code changes are continuously integrated.
    log("Code fetched successfully.")

    if not build_project(): # CI: Automated build
        log("Pipeline stopped due to build failure.", "CRITICAL")
        return

    if not run_tests(): # CI: Automated testing
        log("Pipeline stopped due to test failure.", "CRITICAL")
        return

    log("CI phase completed successfully. Artifacts ready for deployment.", "PIPELINE")

    # 2. Continuous Delivery/Deployment (CD) part
    if not deploy_to_staging(): # CD: Automated deployment to staging
        log("Pipeline stopped due to staging deployment failure.", "CRITICAL")
        return

    log("Staging environment ready. Awaiting manual approval or automated gate for production deployment...", "PIPELINE")
    # In a real CD pipeline, there might be a pause here for manual testing/approval.
    # For this example, we'll proceed directly to demonstrate the full flow.
    time.sleep(2) # Simulate a pause

    log("Proceeding with production deployment...", "PIPELINE")
    deploy_to_production() # CD: Automated deployment to production (or manual trigger for CD)

    log("--- CI/CD Pipeline Completed Successfully ---", "PIPELINE")

if __name__ == "__main__":
    print("\nWelcome to the CI/CD Pipeline Simulator!")
    print("---------------------------------------")
    print("You can configure failures by changing SIMULATE_*_FAILURE flags at the top of the script.")
    print(f"Current configuration: Build Failure={SIMULATE_BUILD_FAILURE}, Test Failure={SIMULATE_TEST_FAILURE}, Staging Deploy Failure={SIMULATE_DEPLOY_STAGING_FAILURE}")
    print("---------------------------------------")
    run_ci_cd_pipeline()
    print("\n")
