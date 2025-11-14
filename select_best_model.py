import re
import shutil

logfile = "build_loop.log"
best_model = None
best_score = float('inf')

with open(logfile) as f:
    for line in f:
        m = re.match(r'\s*(\S+\.pdb)\s+([-+]?\d*\.\d+|\d+)', line)
        if m:
            model = m.group(1)
            score = float(m.group(2))
            if score < best_score:
                best_score = score
                best_model = model

if best_model:
    print(f"Best model: {best_model} (score = {best_score:.4f})")

    # Copy with both filenames for convenience
    shutil.copy(best_model, "best_loop_model.pdb")
    shutil.copy(best_model, "best_model.pdb")
    print("Copied to best_loop_model.pdb and best_model.pdb")
else:
    print("No models found — check build_loop.log for format or errors.")
