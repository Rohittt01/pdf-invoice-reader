# import os
# from PIL import Image

# output_dir = "./pdfs"
# source_dir = "./images"

# for file in os.listdir(source_dir):
#     if file.split(".")[-1] in ("png", "jpg", "jpeg"):
#         image = Image.open(os.path.join(source_dir, file))
#         image_converted = image.convert("RGB")
#         image_converted.save(os.path.join(output_dir, "{0}.pdf".format(file.split(".")[-2])))
import os
from PIL import Image

output_dir = "./pdfs"
source_dir = "./images"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(source_dir):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(source_dir, file)
        base_name, ext = os.path.splitext(file)

        try:
            image = Image.open(image_path)
            image_converted = image.convert("RGB")
            pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
            image_converted.save(pdf_path)
            print(f"Converted {file} to {pdf_path}")
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

# import os
from PyPDF2 import PdfMerger

output_dir = "./pdfs"
merged_pdf_path = "./merged.pdf"

# Get a list of PDF files in the output directory
pdf_files = [os.path.join(output_dir, file) for file in os.listdir(output_dir) if file.lower().endswith(".pdf")]

# Create a PdfFileMerger object
pdf_merger = PdfMerger()

# Merge the PDF files into a single PDF
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# Write the merged PDF to a file
pdf_merger.write(merged_pdf_path)

# Close the PdfFileMerger object
pdf_merger.close()

print(f"Merged PDF saved to {merged_pdf_path}")


