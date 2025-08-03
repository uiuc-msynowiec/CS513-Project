import os
import subprocess
import graphviz

def convert_yw_file(filename, yw_jar="yesworkflow-0.2.0-jar-with-dependencies.jar"):
    base_name = os.path.splitext(os.path.basename(filename))[0]
    py_name = f"{base_name}.py"
    dot_name = f"{base_name}.dot"
    png_name = f"{base_name}.png"

    print(f"Processing {py_name}...")
    try:
        command = f"java -jar {yw_jar} graph {py_name} > {dot_name}"
        subprocess.run(command, shell=True, check=True)
        print(f"Created {dot_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating .dot from {py_name} using Java JAR: {e}")

    try:
        with open(dot_name, "r", encoding="utf-8") as f:
            dot_data = f.read()
        graph = graphviz.Source(dot_data)
        graph.render(base_name, format="png", cleanup=True)
        print(f"Rendered {png_name}")
    except Exception as e:
        print(f"Error rendering PNG for {filename}: {e}")

convert_yw_file("W1_outer_workflow.py")