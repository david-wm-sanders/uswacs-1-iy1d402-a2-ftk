import sys

md5h, sha1h = sys.argv[1], sys.argv[2]

print(r"{")
print(r"\ttfamily\tiny")
print(r"\begin{flushright}")
print(f"MD5:{md5h}")
print(r"\end{flushright}")
print(r"\vspace{-4em}")
print(r"}")

print(r"\begin{table}[h!]")
print(r"\ttfamily\footnotesize")
print(r"\setlength{\tabcolsep}{0.1cm}")
print(r"\newcolumntype{k}{p{1cm}}")
print(r"\newcolumntype{v}{c}")
print(r"\begin{tabular}{|k|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|}")
print(r"\hline")
md5hs, md5hs_pad = " & ".join(md5h), " & ".join("-" * 8)
print(f"MD5 & {md5hs} & {md5hs_pad} \\tabularnewline \\hline")
sha1hs = " & ".join(sha1h)
print(f"SHA1 & {sha1hs} \\tabularnewline \\hline")
print(r"\end{tabular}")
print(r"\end{table}")

print(r"{")
print(r"\ttfamily\tiny")
print(r"\vspace{-4.5em}")
print(r"\begin{flushright}")
print(f"SHA1:{sha1h}")
print(r"\end{flushright}")
print(r"}")
