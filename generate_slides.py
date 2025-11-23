import json
import os

def generate_slides():
    with open('docs/outline.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    slides = data.get('slides', [])
    
    markdown_content = "---\nmarp: true\npaginate: true\nstyle: |\n  @import url('styles.css');\n---\n\n"
    prompts_data = {"slides": []}

    for i, slide in enumerate(slides):
        slide_num = i + 1
        title = slide.get('title', '')
        subtitle = slide.get('subtitle', '')
        body = slide.get('body', [])
        layout = slide.get('layout', '')
        
        # Generate filename
        safe_title = title.replace(' ', '_').replace('/', '_').replace('：', '_').replace('（', '_').replace('）', '').replace('・', '')
        # Truncate if too long
        if len(safe_title) > 20:
            safe_title = safe_title[:20]
        
        filename = f"{slide_num:02d}_{safe_title}.png"
        
        # Markdown generation
        markdown_content += f"# {title}\n\n"
        
        if subtitle:
            markdown_content += f"## {subtitle}\n\n"
            
        # Add image placeholder
        markdown_content += f"![{title}](assets/illustrations/{filename})\n\n"
        
        if body:
            for item in body:
                markdown_content += f"{item}\n"
            markdown_content += "\n"
            
        markdown_content += "---\n\n"

        # Prompt generation
        prompt = f"Minimal line art illustration for a presentation slide titled '{title}'. "
        if subtitle:
            prompt += f"Subtitle: '{subtitle}'. "
        if body:
            prompt += f"Keywords: {', '.join(body[:3])}. "
        prompt += "Style: minimal, modern, abstract, clean lines, white background."

        prompts_data["slides"].append({
            "id": slide_num,
            "filename": filename,
            "style": "minimal-line-art",
            "prompt": prompt
        })

    # Remove last separator
    markdown_content = markdown_content.rsplit("---\n\n", 1)[0]

    with open('slides.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    with open('assets/prompts/illustration_prompts.json', 'w', encoding='utf-8') as f:
        json.dump(prompts_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_slides()
