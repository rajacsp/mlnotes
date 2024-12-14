---
title: Bokeh-Pynotes-Growth
date: 2024-12-14
author: Your Name
cell_count: 12
score: 10
---

```python
# https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_1.html
```


```python
# https://docs.bokeh.org/en/latest/_images/notebook_inline.png
```


```python
# !pip install jupyter_bokeh
```


```python
!pip show | grep "Version:"
```

    [33mWARNING: ERROR: Please provide a package name or names.[0m[33m
    [0m


```python
# !pip install bokeh
```


```python
x = [1, 2, 3, 4, 5, 6, 7]
```


```python
y = [
    0,
    220,
    380,
    500,
    540,
    540,
    590,
]
```


```python
from bokeh.plotting import figure
from bokeh.io import output_notebook
```


```python
# create a new plot with a title and axis labels
p = figure(
    title         = "My Pynotes Growth", 
    x_axis_label  = 'x', 
    y_axis_label  = 'y'
)
```


```python
# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)
```




<div style="display: table;"><div style="display: table-row;"><div style="display: table-cell;"><b title="bokeh.models.renderers.glyph_renderer.GlyphRenderer">GlyphRenderer</b>(</div><div style="display: table-cell;">id&nbsp;=&nbsp;'p1125', <span id="p1131" style="cursor: pointer;">&hellip;)</span></div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">context_menu&nbsp;=&nbsp;None,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">coordinates&nbsp;=&nbsp;None,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">css_classes&nbsp;=&nbsp;[],</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">css_variables&nbsp;=&nbsp;{},</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">data_source&nbsp;=&nbsp;ColumnDataSource(id='p1119', ...),</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">glyph&nbsp;=&nbsp;Line(id='p1122', ...),</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">group&nbsp;=&nbsp;None,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">hover_glyph&nbsp;=&nbsp;None,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">js_event_callbacks&nbsp;=&nbsp;{},</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">js_property_callbacks&nbsp;=&nbsp;{},</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">level&nbsp;=&nbsp;'glyph',</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">muted&nbsp;=&nbsp;False,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">muted_glyph&nbsp;=&nbsp;Line(id='p1124', ...),</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">name&nbsp;=&nbsp;None,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">nonselection_glyph&nbsp;=&nbsp;Line(id='p1123', ...),</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">propagate_hover&nbsp;=&nbsp;False,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">selection_glyph&nbsp;=&nbsp;'auto',</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">styles&nbsp;=&nbsp;{},</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">stylesheets&nbsp;=&nbsp;[],</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">subscribed_events&nbsp;=&nbsp;PropertyValueSet(),</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">syncable&nbsp;=&nbsp;True,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">tags&nbsp;=&nbsp;[],</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">view&nbsp;=&nbsp;CDSView(id='p1126', ...),</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">visible&nbsp;=&nbsp;True,</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">x_range_name&nbsp;=&nbsp;'default',</div></div><div class="p1130" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">y_range_name&nbsp;=&nbsp;'default')</div></div></div>
<script>
(function() {
  let expanded = false;
  const ellipsis = document.getElementById("p1131");
  ellipsis.addEventListener("click", function() {
    const rows = document.getElementsByClassName("p1130");
    for (let i = 0; i < rows.length; i++) {
      const el = rows[i];
      el.style.display = expanded ? "none" : "table-row";
    }
    ellipsis.innerHTML = expanded ? "&hellip;)" : "&lsaquo;&lsaquo;&lsaquo;";
    expanded = !expanded;
  });
})();
</script>





```python
# show the results
show(p, notebook_handle=True)
```

    Gtk-Message: 20:33:52.612: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
    
    (opera:4012177): Gtk-WARNING **: 20:33:52.668: GTK+ module /snap/opera/346/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
    GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
    Gtk-Message: 20:33:52.668: Failed to load module "canberra-gtk-module"
    
    (opera:4012177): Gtk-WARNING **: 20:33:52.669: GTK+ module /snap/opera/346/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
    GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
    Gtk-Message: 20:33:52.669: Failed to load module "canberra-gtk-module"
    Fontconfig error: Cannot load default config file: No such file: (null)
    [4012177:4012177:1203/203353.271460:ERROR:interface_endpoint_client.cc(725)] Message 0 rejected by interface blink.mojom.WidgetHost
    [4012177:4012177:1203/203353.272102:ERROR:interface_endpoint_client.cc(725)] Message 2 rejected by interface blink.mojom.Widget
    [4012177:4012177:1203/203353.615034:ERROR:CONSOLE(2)] "Uncaught (in promise) [object Object]", source: chrome://startpage/main.js (2)



```python

```


---
**Score: 10**