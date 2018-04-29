import sys

md5h, sha1h = sys.argv[1], sys.argv[2]

print(r"\begin{table}[h!]")
# print(r"\centering")
print(r"\ttfamily\footnotesize")
print(r"\setlength{\tabcolsep}{0.1cm}")
print(r"\newcolumntype{k}{p{0.75cm}}")
print(r"\newcolumntype{v}{c}")
print(r"\begin{tabular}{|k|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|}")
print(r"\hline")
md5hs, md5hs_pad = " & ".join(md5h.upper()), " & ".join("-" * 8)
print(f"MD5 & {md5hs} & {md5hs_pad} \\tabularnewline \\hline")
sha1hs = " & ".join(sha1h.upper())
print(f"SHA1 & {sha1hs} \\tabularnewline \\hline")
print(r"\end{tabular}")
print(r"\end{table}")
