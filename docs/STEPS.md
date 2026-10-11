# STEP-BY-STEP: Complete the project (follow in order)

Legend: [YOU] = must be done by you (needs your accounts). Everything else is already in this folder.

## STEP 1 [YOU] Jira setup (Exp 6) ~30 min
1. Create a free Jira site at atlassian.com. Create a **Scrum** project, key `STMS`.
2. Import the backlog: Jira Settings > System > External System Import > CSV, upload `docs/jira-backlog.csv`.
   (If import is confusing, just create the 12 issues by hand from that file.)
3. Create 2 sprints. Sprint 1: first 5 stories. Click **Start sprint**.
4. Create Epics if you like: Features, Containerization, CI/CD, Monitoring, Cloud.
5. Install the **GitHub for Jira** app and connect your GitHub account (Step 3).

## STEP 2 [YOU] Put the code in Git (Exp 1) ~20 min
    cd stms
    git init
    git add .
    git commit -m "STMS-1: initial project structure"
Create an empty repo called `stms` on GitHub, then:
    git remote add origin https://github.com/<your-username>/stms.git
    git branch -M main
    git push -u origin main
Now practise the commands in `docs/GIT_COMMANDS.md`. Make **separate branches per Jira ticket**
(`feature/STMS-2-edit-delete`), open Pull Requests, merge them. Put the ticket key in every commit.
Tip: tell yourself "no commit without a Jira key". Your ma'am will see it linked inside Jira.

## STEP 3 [YOU] Link GitHub and Jira
In Jira: Apps > GitHub for Jira > connect your repo. Open any ticket: commits and PRs now show.

## STEP 4 Run the app and tests locally ~5 min
    pip install -r requirements.txt
    cd app && pytest -v
    python app.py     # open http://localhost:5000
Move STMS-1, 2, 3, 4 to Done in Jira.

## STEP 5 Docker (Exp 2) ~15 min
    docker build -t stms:v1 .
    docker run -d -p 5000:5000 --name stms stms:v1
    docker ps
    docker logs stms
    docker stop stms && docker rm stms
Push to Docker Hub [YOU: needs account]:
    docker login
    docker tag stms:v1 <dockerhub-username>/stms:latest
    docker push <dockerhub-username>/stms:latest

## STEP 6 Docker Compose + Monitoring (Exp 3 and 7) ~20 min
    docker compose up -d --build
    docker compose ps          # 3 services running
1. Open the app, add/complete a few tasks to generate traffic.
2. Prometheus http://localhost:9090 > Status > Targets: `stms` is UP.
3. Grafana http://localhost:3000 (admin/admin): dashboard **STMS Monitoring** is already loaded
   (Dashboards > STMS Monitoring). Data source is auto-configured.
Screenshot all three.

## STEP 7 Jenkins (Exp 4) ~30 min
    docker compose -f docker-compose.jenkins.yml up -d --build
    docker logs stms-jenkins        # copy the initial admin password
1. Open http://localhost:8080, paste password, Install suggested plugins, create user.
2. New Item > name `stms-pipeline` > **Pipeline** > OK.
3. Pipeline definition: **Pipeline script from SCM** > Git > your GitHub repo URL > branch `*/main`
   > Script Path `Jenkinsfile` > Save.
4. **Build Now**. Screenshot the Stage View (all green) and Console Output.
5. App deployed by Jenkins is at http://localhost:5001.
(Private repo? Add GitHub credentials in Jenkins. Simplest: keep the repo public.)

## STEP 8 [YOU] GitHub Actions (Exp 5) ~15 min
1. GitHub repo > Settings > Secrets and variables > Actions > New repository secret:
   - `DOCKER_USERNAME` = your Docker Hub username
   - `DOCKER_PASSWORD` = a Docker Hub **access token** (Docker Hub > Account Settings > Security)
2. Push any change to `main`. Open the **Actions** tab: test -> docker jobs go green.
3. The `deploy` job stays skipped until Step 9. That is intentional.

## STEP 9 [YOU] Deploy to AWS (Exp 8) ~30 min
1. AWS Console > EC2 > Launch instance: Ubuntu 22.04, t2.micro, create key pair `stms-key` (download .pem).
2. Security group: allow SSH (22) and Custom TCP 5000.
3. SSH in and install Docker:
       ssh -i stms-key.pem ubuntu@<EC2-IP>
       sudo apt update && sudo apt install -y docker.io
       sudo usermod -aG docker ubuntu
4. GitHub secrets: `EC2_HOST` (public IP), `EC2_KEY` (paste whole .pem file contents).
5. GitHub > Settings > Secrets and variables > Actions > **Variables** tab > new variable
   `ENABLE_DEPLOY` = `true`.
6. Push a small change. All 3 jobs go green. Open http://<EC2-IP>:5000.
7. Terminate this instance before Step 10 (so Terraform can create its own).

## STEP 10 [YOU] Terraform (Exp 9) ~25 min
1. Install Terraform and AWS CLI. Create an IAM user with EC2 permissions, run `aws configure`.
2. Make sure `<dockerhub-username>/stms:latest` exists on Docker Hub (Step 5/8).
       cd terraform
       cp terraform.tfvars.example terraform.tfvars   # edit with your values
       terraform init
       terraform plan
       terraform apply         # type yes
       terraform output app_url
3. Open the URL (wait 2-3 min for Docker to start). Screenshot plan, apply, AWS console.
4. **Clean up to avoid charges:** `terraform destroy`

## STEP 11 Final submission checklist
- [ ] Jira: sprint board, backlog, completed sprint, burndown chart, ticket with linked commits
- [ ] GitHub: 15+ commits with Jira keys, branches, 2+ merged Pull Requests, tag v1.0, green Actions runs
- [ ] Docker Hub image page + `docker ps` + `docker compose ps`
- [ ] Jenkins green Stage View
- [ ] Prometheus targets UP + Grafana dashboard with live data
- [ ] App running on AWS IP
- [ ] Terraform plan/apply/destroy screenshots
- [ ] README.md in repo
Complete and close Sprint 1 in Jira before your viva so the burndown chart has data.
