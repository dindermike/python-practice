# Use this file to generate HTML Files that embed Python Files as display code on that page, for educational and
# resume purposes only.
from os import listdir, path
from os.path import isfile, join


def generate_html_with_code(python_file_path, output_html_path):
    try:
        with open(python_file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()

        # HTML Template with <pre> and <code> Tags
        html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <!-- Character Encoding -->
                    <meta charset="UTF-8">

                    <!-- Viewport for Responsive Design -->
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">

                    <!-- Page Title -->
                    <title>Python {python_file_path} Source Code</title>

                    <!-- Meta Description for SEO -->
                    <meta name="description" content="A practice code page for displaying {python_file_path} python snippets.">  # noqa: E501

                    <!-- Meta Keywords -->
                    <meta name="keywords" content="code, snippets, python, programming, syntax highlighting, development">  # noqa: E501

                    <!-- Author Information -->
                    <meta name="author" content="Mike Dinder">

                    <!-- HTTP Equiv Headers -->
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

                    <!-- Robots Meta Tag -->
                    <meta name="robots" content="index, follow">

                    <!-- Open Graph Meta Tags for Social Media -->
                    <meta property="og:title" content="Display {python_file_path} Code Snippets">
                    <meta property="og:description" content="A practice code page for displaying {python_file_path} python snippets.">  # noqa: E501
                    <meta property="og:type" content="website">
                    <meta property="og:url" content="https://www.mikedinder.com/{output_html_path}">
                    <meta property="og:image" content="https://www.mikedinder.com/mikedinder.jpg">

                    <!-- Twitter Card Meta Tags -->
                    <meta name="twitter:card" content="summary_large_image">
                    <meta name="twitter:title" content="Display {python_file_path} Code Snippets">
                    <meta name="twitter:description" content="A practice code page for displaying {python_file_path} python snippets.">
                    <meta name="twitter:image" content="https://www.mikedinder.com/mikedinder.jpg">

                    <!-- Favicon -->
                    <link rel="icon" type="image/x-icon" href="/favicon.ico">
                    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

                    <!-- Theme Color for Mobile Browsers -->
                    <meta name="theme-color" content="#1e293b">

                    <!-- Preconnect to CDN for Performance -->
                    <!-- <link rel="preconnect" href="https://cdnjs.cloudflare.com"> -->

                    <!-- Highlight.js for Syntax Highlighting -->
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

                    <style type="text/css">
                        body {{ font-family: monospace; }}
                        pre {{ background-color: #f4f4f4; padding: 1em; border: 1px solid #ddd; color: #000000; }}
                        h2 {{ color: #000000; font-weight: bold; font-size: 1em; }}
                    </style>

                    <!-- Custom Styles -->
                    <style>
                        * {
                            margin: 0;
                            padding: 0;
                            box-sizing: border-box;
                        }
                        
                        body {
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                            line-height: 1.6;
                            color: #e2e8f0;
                            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
                            min-height: 100vh;
                            padding: 20px;
                        }
                        
                        .container {
                            max-width: 1200px;
                            margin: 0 auto;
                        }
                        
                        header {
                            text-align: center;
                            margin-bottom: 40px;
                            padding: 20px;
                        }
                        
                        h1 {
                            font-size: 2.5rem;
                            color: #60a5fa;
                            margin-bottom: 10px;
                        }
                        
                        .subtitle {
                            color: #94a3b8;
                            font-size: 1.1rem;
                        }
                        
                        .snippet-container {
                            background: #1e293b;
                            border-radius: 12px;
                            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                            margin-bottom: 30px;
                            overflow: hidden;
                            border: 1px solid #334155;
                        }
                        
                        .snippet-header {
                            background: #0f172a;
                            padding: 15px 20px;
                            border-bottom: 1px solid #334155;
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                        }
                        
                        .snippet-title {
                            color: #f1f5f9;
                            font-size: 1.1rem;
                            font-weight: 600;
                        }
                        
                        .language-badge {
                            background: #3b82f6;
                            color: white;
                            padding: 5px 12px;
                            border-radius: 20px;
                            font-size: 0.85rem;
                            font-weight: 500;
                        }
                        
                        .snippet-body {
                            position: relative;
                        }
                        
                        pre {
                            margin: 0;
                            padding: 20px;
                            overflow-x: auto;
                        }
                        
                        code {
                            font-family: 'Courier New', Courier, monospace;
                            font-size: 0.95rem;
                        }
                        
                        .copy-button {
                            position: absolute;
                            top: 10px;
                            right: 10px;
                            background: #3b82f6;
                            color: white;
                            border: none;
                            padding: 8px 16px;
                            border-radius: 6px;
                            cursor: pointer;
                            font-size: 0.9rem;
                            transition: background 0.3s ease;
                        }
                        
                        .copy-button:hover {
                            background: #2563eb;
                        }
                        
                        .copy-button:active {
                            background: #1d4ed8;
                        }
                        
                        footer {
                            text-align: center;
                            margin-top: 50px;
                            padding: 20px;
                            color: #64748b;
                        }
                        
                        @media (max-width: 768px) {
                            h1 {
                                font-size: 2rem;
                            }
                            
                            .snippet-header {
                                flex-direction: column;
                                gap: 10px;
                                align-items: flex-start;
                            }
                        }
                    </style>
                </head>
                <body>
                    <h2>Source Code of "{python_file_path}"</h2>
                    <pre><code>{code_content}</code></pre>

                    <!-- Initialize Highlight.js -->
                    <script>
                        // Initialize syntax highlighting
                        hljs.highlightAll();

                        // Copy code function
                        function copyCode(button) {{
                            const codeBlock = button.nextElementSibling.querySelector('code');
                            const code = codeBlock.textContent;

                            navigator.clipboard.writeText(code).then(() => {{
                                const originalText = button.textContent;
                                button.textContent = 'Copied!';
                                button.style.background = '#10b981';

                                setTimeout(() => {{
                                    button.textContent = originalText;
                                    button.style.background = '#3b82f6';
                                }}, 2000);
                            }}).catch(err => {{
                                console.error('Failed to copy code:', err);
                                button.textContent = 'Error!';
                                button.style.background = '#ef4444';

                                setTimeout(() => {{
                                    button.textContent = 'Copy';
                                    button.style.background = '#3b82f6';
                                }}, 2000);
                            }});
                        }}
                    </script>
                </body>
            </html>
        """

        with open('/home/mike/Python_Practice/Generated_HTML/' + output_html_path, 'w', encoding='utf-8') as f_html:
            f_html.write(html_content)

        print(f"Generated HTML File: {output_html_path}")

    except FileNotFoundError:
        print(f"Error: The File '{python_file_path}' Was Not Found.")
    except Exception as e:
        print(f"An Error Occurred: {e}")


if __name__ == '__main__':
    directory1 = '/home/mike/Python_Practice'
    directory2 = '/home/mike/Python_Practice/Requests'
    directory3 = '/home/mike/Python_Practice/SQL_Practice'

    files_list1 = [f for f in listdir(directory1) if isfile(join(directory1, f))]
    files_list2 = [f for f in listdir(directory2) if isfile(join(directory2, f))]
    files_list3 = [f for f in listdir(directory3) if isfile(join(directory3, f))]

    files_list = files_list1 + files_list2 + files_list3

    print(files_list)

    # for file in files_list:
    #     file_extension = file.split('.')

    #     if file_extension == 'py':
    #         generate_html_with_code(file, file + '.html')

# Example usage:
# generate_html_with_code('my_script.py', 'code_output.html')
