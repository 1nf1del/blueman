#
#
# blueman
# (c) 2008 Valmantas Paliksa <walmis at balticum-tv dot lt>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
def _(a):
	return a

class manager_toolbar:

	def __init__(self, blueman):
		self.blueman = blueman
		
		self.blueman.List.connect("device-selected", self.on_device_selected)
		self.blueman.List.connect("device-property-changed", self.on_device_propery_changed)
		
		self.b_bond = blueman.Builder.get_object("b_bond")
		self.b_trust = blueman.Builder.get_object("b_trust")
		self.b_remove = blueman.Builder.get_object("b_remove")
		self.b_add = blueman.Builder.get_object("b_add")
		self.b_setup = blueman.Builder.get_object("b_setup")
		
		
		
		
	def on_device_selected(self, dev_list, device, iter):
		if device == None or iter == None:
			self.b_bond.props.sensitive = False
			self.b_remove.props.sensitive = False
			self.b_trust.props.sensitive = False
			self.b_setup.props.sensitive = False
			self.b_add.props.sensitive = False
		else:
			row = dev_list.get(iter, "bonded", "trusted", "fake")
			self.b_setup.props.sensitive = True
			if row["bonded"]:
				self.b_bond.props.sensitive = False
			else:
				self.b_bond.props.sensitive = True
			
			if row["trusted"]:
				self.b_trust.props.sensitive = True
				self.b_trust.props.stock_id = "gtk-no"
				self.b_trust.props.label = _("Untrust")
			else:
				self.b_trust.props.sensitive = True
				self.b_trust.props.stock_id = "gtk-yes"
				self.b_trust.props.label = _("Trust")
			
			if row["fake"]:
				self.b_remove.props.sensitive = False
				self.b_add.props.sensitive = True
			
				self.b_bond.props.sensitive = True
			else:
				self.b_remove.props.sensitive = True
			
	def on_device_propery_changed(self, dev_list, device, iter, kv):
		(key, value) = kv
		if key == "Trusted" or key == "Paired":
			if dev_list.compare(iter, dev_list.selected()):
				self.on_device_selected(dev_list, device, iter)
				
		elif key == "Fake":
			if not value:
				self.b_remove.props.sensitive = True
			else:
				self.b_remove.props.sensitie = False
				
		
		
