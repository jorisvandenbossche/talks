library(xaringanthemer)

style_duo_accent(
  padding = "96px 64px 64px 64px", # little extra at the top
  primary_color      = "#005050", # Voltron Data primary green 
  secondary_color    = "#d9d8d6", # Voltron Data primary light grey
  header_font_google = google_font("Roboto"),
  link_color         = "#f97b64", # orange links (complements nicely with all three colour schemes)
  text_font_google   = google_font("Roboto", "300", "300i"),
  code_font_google   = google_font("Fira Code"),
  text_font_size     = "30px",
  outfile            = here::here("style", "xaringan-themer.css")
)
