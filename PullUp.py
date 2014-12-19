import sublime, sublime_plugin

class PullUpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.line(4)
		# THe row of the current cursor
		(row, col) = self.view.rowcol(self.view.sel()[0].begin())
		#print row
		active_view = sublime.active_window().active_view()
		active_region = active_view.visible_region()
		(viewport_x, viewport_y) = active_view.viewport_position()


		viewRegion = sublime.Region(0, self.view.size())  
		print (viewRegion.lines())

#		self.view.replace(edit, viewRegion, '#test')
		print viewport_x
		print active_region
		print active_view.lines(active_region)

		#self.view.insert(edit, 0, "Hello, World!")

