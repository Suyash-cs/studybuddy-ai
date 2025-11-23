import time
from datetime import datetime
def llm_simulator(prompt):
   
    prompt = prompt.lower()

    if "analyze" in prompt:
        return (
            "Here's what I noticed from your study pattern:\n"
            "- You seem to focus better during morning hours.\n"
            "- Short and crisp sessions keep you productive.\n"
            "- Math & Coding need a bit more attention.\n"
            "- You lose focus when sessions go longer than 90 minutes.\n"
            "\nDon’t worry — I’ll create a plan that fits your style 👍"
        )

    if "create" in prompt or "study plan" in prompt or "plan" in prompt:
        return (
            "Alright! I’ve put together a balanced and realistic study plan for you:\n\n"
            "📘 Math — 1.5 hours (fresh mind = better problem solving)\n"
            "🔭 Physics — 1 hour (numericals practice)\n"
            "🇩🇪 German — 30 mins (light vocabulary revision)\n"
            "💻 Coding — 1.5 hours (project practice)\n\n"
            "✨ Total Study Time = 4.5 hours\n"
            "This looks like a solid, productive day! Let’s go 🚀"
        )

    return "Hey! I'm StudyBuddy 👋 Tell me what you need help with today."

class MemoryStore:
    def _init_(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def load(self, key, default=None):
        return self.data.get(key, default)

memory = MemoryStore()

def calculate_minutes(text):
    text = text.lower().strip()

    if "hour" in text:
        num = float(text.split()[0])
        return int(num * 60)

    if "min" in text:
        return int(text.split()[0])

    return 0

class StudyAgent:
    def _init_(self, llm):
        self.llm = llm

    def analyze_user(self):
        result = self.llm("Analyze the user's study habits")
        memory.save("analysis", result)
        return result

    def generate_plan(self, subjects):
        prompt = f"Create a study plan for these subjects: {subjects}"
        plan = self.llm(prompt)
        memory.save("last_plan", plan)
        return plan

class ProgressLoop:
    def _init_(self, interval=2):
        self.interval = interval

    def run(self):
        print("\n🔄 Starting Progress Tracker...\n")
        messages = [
            "You're doing great — keep going! 💪",
            "Small steps = Big results. Stay consistent! ✨",
            "Focus for a few more minutes. You got this! 🔥"
        ]
        for i in range(3):
            print(f"⏳ Reminder {i+1}: {messages[i]}")
            time.sleep(self.interval)
        print("\n✔ Progress tracker completed.\n")

class StudyBuddySystem:
    def _init_(self, agent, loop):
        self.agent = agent
        self.loop = loop

    def run(self, subjects):
        print("🔹 Step 1: Understanding Your Study Pattern...\n")
        print(self.agent.analyze_user())
        print("\n-------------------------------------------------\n")

        print("🔹 Step 2: Building Your Personalized Study Plan...\n")
        plan = self.agent.generate_plan(subjects)
        print(plan)
        print("\n-------------------------------------------------\n")

        print("🔹 Step 3: Keeping You Motivated...\n")
        self.loop.run()

        return plan


subjects = ["Math", "Physics", "German", "Coding"]

agent = StudyAgent(llm_simulator)
loop = ProgressLoop(interval=1)

system = StudyBuddySystem(agent, loop)
study_plan = system.run(subjects)

print("🔹 Calculating Total Study Minutes...\n")

time_list = ["1.5 hours", "1 hour", "30 mins", "1.5 hours"]
total = sum(calculate_minutes(t) for t in time_list)

print(f"⏱️ Total Study Time = {total} minutes")
print("\nAll set! Your StudyBuddy agent is ready to use anytime 😄")
