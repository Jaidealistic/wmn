import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def sanitize(text):
    # Remove AI-like em-dashes and formatting artifacts
    text = text.replace('—', '-')
    text = text.replace('–', '-')
    return text.strip()

doc = docx.Document()

# Set default font
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)

# --- HEADER SECTION ---
header_p = doc.add_paragraph()
header_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = header_p.add_run(sanitize("COURSE CODE: 23CSE401\nCOURSE NAME: Fundamentals of Artificial Intelligence\nNAME: Jai Subiksha T\nROLL NO: CB.SC.U4CSE23327"))
r.bold = True
r.font.size = Pt(12)

doc.add_paragraph() # spacing

# --- MAIN TITLE ---
title = doc.add_heading(level=1)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
tr = title.add_run(sanitize("CONSTRAINT SATISFACTION PROBLEMS (CSP)"))
tr.font.name = 'Times New Roman'
tr.font.color.rgb = RGBColor(0, 0, 0)
tr.bold = True

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
sr = subtitle.add_run(sanitize("Practical Problems, Modelling, and Backtracking Concepts"))
sr.font.name = 'Times New Roman'
sr.font.size = Pt(14)
sr.italic = True

doc.add_paragraph() # spacing

# --- HELPERS ---
def add_heading2(text):
    p = doc.add_heading(level=2)
    r = p.add_run(sanitize(text))
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(0, 0, 0)
    r.bold = True

def add_heading3(text):
    p = doc.add_heading(level=3)
    r = p.add_run(sanitize(text))
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(0, 0, 0)
    r.bold = True

def add_para(text, bold_prefix=None):
    p = doc.add_paragraph()
    if bold_prefix:
        p.add_run(sanitize(bold_prefix)).bold = True
        p.add_run(" " + sanitize(text))
    else:
        p.add_run(sanitize(text))

def add_bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(sanitize(text))

def add_math(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(sanitize(text))
    r.font.name = 'Courier New'
    r.italic = True

# --- SECTION 1 ---
add_heading2("1. CSP Example: University Course Registration")
add_para("(Demonstrating Unary, Binary, Ternary Constraints, and Consistency Models)")
add_para("University course registration is a standard practical example of a Constraint Satisfaction Problem (CSP) other than map coloring. In this scenario, a student selects an academic schedule across available sections while satisfying degree prerequisites, department guidelines, and timetable constraints.")

add_heading3("Variables")
add_para("Let each course selected by the student be a decision variable:")
add_bullet("C1: CSE401 (Compiler Design)")
add_bullet("C2: CSE402 (Distributed Systems)")
add_bullet("C3: CSE403 (Cyber Security)")
add_bullet("C4: CSE404 (Software Engineering)")

add_heading3("Domains")
add_para("The domain of each variable consists of the available class time slots for that specific course:")
add_bullet("Domain(C1) = {Monday 9 AM, Wednesday 2 PM, Friday 11 AM}")
add_bullet("Domain(C2) = {Monday 9 AM, Tuesday 10 AM, Thursday 3 PM}")
add_bullet("Domain(C3) = {Monday 9 AM, Tuesday 10 AM, Wednesday 2 PM}")
add_bullet("Domain(C4) = {Tuesday 10 AM, Thursday 3 PM, Friday 11 AM}")

add_heading3("Constraints")
add_para("Unary Constraint (Constrains a single variable):", bold_prefix="Unary Constraint:")
add_bullet("C1 != Wednesday 2 PM (The Wednesday 2 PM section of CSE401 is reserved exclusively for another department).")

add_para("Binary Constraint (Constrains a pair of variables):", bold_prefix="Binary Constraint:")
add_bullet("C1 != C2 (The student cannot be enrolled in CSE401 and CSE402 during the same time slot).")
add_bullet("C2 != C3 (CSE402 and CSE403 cannot share an identical lecture slot).")

add_para("Ternary Constraint (Constrains three variables simultaneously):", bold_prefix="Ternary Constraint:")
add_bullet("Valid(C1, C2, C3): If courses C1, C2, and C3 are scheduled on the same day (such as Monday), their combined practical lab hours across all three courses must not exceed 6 hours in that single day:")
add_math("LabHours(C1) + LabHours(C2) + LabHours(C3) <= 6")

add_heading3("Consistency Implementations")
add_para("Node Consistency (1-Consistency):", bold_prefix="Node Consistency:")
add_bullet("A variable satisfies node consistency if all values in its domain satisfy its unary constraints.")
add_bullet("Application: For variable C1, evaluating the unary constraint (C1 != Wednesday 2 PM) removes 'Wednesday 2 PM' directly from its domain:")
add_math("Domain(C1) -> {Monday 9 AM, Friday 11 AM}")

add_para("Arc Consistency (2-Consistency / AC-3):", bold_prefix="Arc Consistency:")
add_bullet("A directed arc (Ci -> Cj) is arc-consistent if for every value x in Domain(Ci), there is at least one allowable value y in Domain(Cj) that satisfies the binary constraint between them.")
add_bullet("Application: Take the binary constraint C1 != C2. If Domain(C1) is reduced to {Monday 9 AM} and Domain(C2) is also {Monday 9 AM}, assigning Monday 9 AM to C1 leaves zero valid options for C2. Arc consistency prunes such impossible values before branching.")

add_para("k-Consistency:", bold_prefix="k-Consistency:")
add_bullet("For any set of k - 1 variables that have mutually consistent assignments, any k-th variable can always be assigned a value satisfying all constraints across the k variables.")
add_bullet("Application: 1-consistency corresponds to Node Consistency. 2-consistency corresponds to Arc Consistency. 3-consistency corresponds to Path Consistency, which guarantees that for any valid assignment to (C1, C2), there exists an assignment for C3 that is simultaneously compatible with both C1 and C2.")
add_bullet("If a network is strongly k-consistent, a solution can be generated systematically without backtracking.")

doc.add_page_break()

# --- SECTION 2 ---
add_heading2("2. Real-Life CSP: Hospital Nurse Shift Scheduling")
add_para("(Formulation and the AllDifferent Global Constraint)")
add_para("Preparing a weekly duty roster for nurses in a hospital ward requires assigning qualified healthcare workers to distinct shifts while satisfying staffing ratios, medical qualifications, and work-hour regulations.")

add_heading3("Variables")
add_para("Let each shift requirement on the roster be a variable:")
add_bullet("S1: Monday Morning Shift")
add_bullet("S2: Monday Afternoon Shift")
add_bullet("S3: Monday Night Shift")
add_bullet("S4: Tuesday Morning Shift")

add_heading3("Domains")
add_para("The domain of each variable contains the qualified nurses available for assignment:")
add_bullet("Domain(Si) = {Nurse Anu, Nurse Priya, Nurse Kavya, Nurse Deepa}")

add_heading3("Constraints")
add_bullet("Availability Constraint (Unary): Nurse Anu is on approved medical leave on Monday, meaning Nurse Anu is removed from Domain(S1), Domain(S2), and Domain(S3).")
add_bullet("Rest Interval Constraint (Binary): A nurse assigned to the Monday Night Shift (S3) cannot work the consecutive Tuesday Morning Shift (S4) to ensure mandatory recovery time: S3 != S4.")
add_bullet("Workload Constraint: A nurse must not be scheduled for more than 5 shifts within a single week.")

add_heading3("Applying the AllDifferent Global Constraint")
add_para("A global constraint encapsulates a relation over an arbitrary number of variables rather than decomposing the condition into simple pairs.")
add_bullet("Definition: AllDifferent(V1, V2, ..., Vm) specifies that all variables in the given set must take mutually distinct values:")
add_math("For all i != j, Vi != Vj")
add_bullet("Application in Nurse Scheduling: During peak morning operations, four key posts must be managed simultaneously by distinct staff members: Emergency Triage (T), Intensive Care (I), Operation Theatre (O), and Pediatric Ward (P). Rather than writing separate binary inequality pairs (T != I, T != O, T != P, I != O, etc.), we apply:")
add_math("AllDifferent(T, I, O, P)")
add_bullet("Advantage: Global constraints use dedicated filtering algorithms (such as bipartite graph matching) to prune domains more aggressively than individual binary checks, exposing unviable assignments early in the search.")

doc.add_page_break()

# --- SECTION 3 ---
add_heading2("3. CSP and Backtracking Concepts with Real-World Examples")

add_heading3("i) Domain Filtering and Value Propagation")
add_bullet("Concept: Domain filtering removes invalid values from a variable's domain based on constraints. Value propagation immediately communicates an assignment to linked variables, pruning their respective domains.")
add_bullet("Example (Food Delivery Logistics): Delivery orders are assigned to active riders. Order A requires a heavy commercial transport permit. Domain filtering eliminates riders lacking this permit, leaving Domain(Order A) = {Rider 2, Rider 5}. Once Rider 2 is assigned to Order A, value propagation removes Rider 2 from the domains of all other simultaneous orders.")

add_heading3("ii) Constraint Propagation and Forward Checking")
add_bullet("Concept: Forward checking monitors domain changes in unassigned variables immediately after a variable is set. If any variable's domain becomes empty, the solver detects an unviable path and triggers backtracking.")
add_bullet("Example (Conference Presentation Scheduling): Project teams are allocated time slots. Team A is assigned the Monday 10 AM slot. Forward checking propagates this constraint to Team B and Team C (who share common faculty reviewers), stripping Monday 10 AM from their domains. If Team B had only Monday 10 AM left, its domain becomes empty, causing the solver to reject Team A's assignment and backtrack immediately.")

add_heading3("iii) Conflict Set and Intelligent Backtracking")
add_bullet("Concept: Standard chronological backtracking reverts to the immediate previous decision variable on failure. Intelligent backtracking (backjumping) maintains a conflict set, which records the variables directly causing the dead end, and jumps straight back to the true source of conflict.")
add_bullet("Example (Lab Computer Allocation for Practical Exams): Student X cannot be assigned any computer because Student Y and Student Z have taken the only available specialized hardware systems. Instead of stepping back through unrelated students who were assigned standard machines, the conflict set identifies {Student Y, Student Z}. The solver jumps back directly to reassign Student Y or Student Z.")

add_heading3("iv) Most Restricted Variable (MRV) Heuristic")
add_bullet("Concept: Often called the Fail-First heuristic, MRV selects the unassigned variable with the fewest remaining legal values in its domain. This keeps the branching factor low and flags dead ends quickly.")
add_bullet("Example (Airport Gate Allocation): An air traffic control system assigns gates to incoming flights. A standard Boeing 737 can use any of 10 gates, whereas an Airbus A380 fits only into Gate 3 or Gate 7 due to double-decker boarding bridges. Under MRV, the scheduler assigns the Airbus A380 first because its domain has only 2 options, preventing other aircraft from inadvertently occupying those specific gates.")

add_heading3("v) Degree Heuristic")
add_bullet("Concept: Used as a tie-breaker alongside MRV, the degree heuristic picks the variable involved in the largest number of constraints with other unassigned variables, placing the most restrictions on the remaining search space.")
add_bullet("Example (Campus Club Meeting Scheduling): Student clubs need weekly meeting slots. The Coding Club shares members with 6 other unassigned clubs, whereas the Chess Club shares members with only 1. If both clubs have 2 remaining open time slots, the degree heuristic selects the Coding Club first to quickly propagate restrictions across the schedule.")

add_heading3("vi) Constraint Weighting and Intelligent Node Selection")
add_bullet("Concept: Hard or frequently violated constraints receive higher numerical weights during search. Intelligent node selection uses these weights to prioritize states that satisfy critical constraints first, steering the search away from problematic regions.")
add_bullet("Example (Factory Equipment Maintenance): Technicians are assigned to maintain factory machinery. Constraints for hazardous chemical reactor units receive high weights due to mandatory safety compliance. Constraints for general assembly conveyors receive standard weights. The solver evaluates high-weight reactor nodes first, ensuring safety parameters are satisfied before processing routine maintenance tasks.")

output_file = r"c:\Users\jaisu\Projects\wmn\AI_CSP_Assignment.docx"
doc.save(output_file)
print(f"Successfully generated {output_file}")
