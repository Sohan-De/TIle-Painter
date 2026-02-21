$utf8 = [System.Text.Encoding]::UTF8
$template = [System.IO.File]::ReadAllText("peintre-revigny-sur-ornain.html", $utf8)

# ---- Vitry-le-Francois ----
$out = $template.Replace("Revigny-sur-Ornain", "Vitry-le-François")
$out = $out.Replace("image/image_2_1.jpg", "image/image_3_1.jpg")
$out = $out.Replace("image/gallery_3.jpg",  "image/gallery_7.jpg")
$out = $out.Replace("image/image_105_1.jpg","image/gallery_4.jpg")
[System.IO.File]::WriteAllText("peintre-vitry-le-francois.html", $out, $utf8)
Write-Host "Fixed: peintre-vitry-le-francois.html"

# ---- Châlons-en-Champagne ----
$out2 = $template.Replace("Revigny-sur-Ornain", "Châlons-en-Champagne")
# images stay the same as Revigny (image_2_1, gallery_3, image_105_1)
[System.IO.File]::WriteAllText("peintre-falons-en-champagne.html", $out2, $utf8)
Write-Host "Fixed: peintre-falons-en-champagne.html"

Write-Host "All encoding fixes applied!"
