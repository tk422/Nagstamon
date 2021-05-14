# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nagstamon/QUI/settings_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_server(object):
    def setupUi(self, settings_server):
        settings_server.setObjectName("settings_server")
        settings_server.resize(659, 1231)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings_server.sizePolicy().hasHeightForWidth())
        settings_server.setSizePolicy(sizePolicy)
        settings_server.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(settings_server)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_password = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 8, 0, 1, 1)
        self.input_lineedit_monitor_url = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_monitor_url.setInputMask("")
        self.input_lineedit_monitor_url.setObjectName("input_lineedit_monitor_url")
        self.gridLayout.addWidget(self.input_lineedit_monitor_url, 4, 2, 1, 2)
        self.label_name = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 3, 0, 1, 1)
        self.input_lineedit_username = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_username.setObjectName("input_lineedit_username")
        self.gridLayout.addWidget(self.input_lineedit_username, 6, 2, 1, 1)
        self.input_lineedit_monitor_cgi_url = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_monitor_cgi_url.setObjectName("input_lineedit_monitor_cgi_url")
        self.gridLayout.addWidget(self.input_lineedit_monitor_cgi_url, 5, 2, 1, 2)
        self.input_combobox_type = QtWidgets.QComboBox(settings_server)
        self.input_combobox_type.setObjectName("input_combobox_type")
        self.gridLayout.addWidget(self.input_combobox_type, 1, 2, 1, 1)
        self.input_lineedit_password = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_lineedit_password.setObjectName("input_lineedit_password")
        self.gridLayout.addWidget(self.input_lineedit_password, 8, 2, 1, 1)
        self.input_checkbox_use_proxy = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_use_proxy.setObjectName("input_checkbox_use_proxy")
        self.gridLayout.addWidget(self.input_checkbox_use_proxy, 17, 0, 1, 1)
        self.groupbox_proxy = QtWidgets.QGroupBox(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_proxy.sizePolicy().hasHeightForWidth())
        self.groupbox_proxy.setSizePolicy(sizePolicy)
        self.groupbox_proxy.setObjectName("groupbox_proxy")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupbox_proxy)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_proxy_password = QtWidgets.QLabel(self.groupbox_proxy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_proxy_password.sizePolicy().hasHeightForWidth())
        self.label_proxy_password.setSizePolicy(sizePolicy)
        self.label_proxy_password.setObjectName("label_proxy_password")
        self.gridLayout_2.addWidget(self.label_proxy_password, 3, 0, 1, 1)
        self.label_proxy_username = QtWidgets.QLabel(self.groupbox_proxy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_proxy_username.sizePolicy().hasHeightForWidth())
        self.label_proxy_username.setSizePolicy(sizePolicy)
        self.label_proxy_username.setObjectName("label_proxy_username")
        self.gridLayout_2.addWidget(self.label_proxy_username, 2, 0, 1, 1)
        self.input_lineedit_proxy_username = QtWidgets.QLineEdit(self.groupbox_proxy)
        self.input_lineedit_proxy_username.setObjectName("input_lineedit_proxy_username")
        self.gridLayout_2.addWidget(self.input_lineedit_proxy_username, 2, 1, 1, 1)
        self.input_lineedit_proxy_address = QtWidgets.QLineEdit(self.groupbox_proxy)
        self.input_lineedit_proxy_address.setObjectName("input_lineedit_proxy_address")
        self.gridLayout_2.addWidget(self.input_lineedit_proxy_address, 1, 1, 1, 1)
        self.label_proxy_address = QtWidgets.QLabel(self.groupbox_proxy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_proxy_address.sizePolicy().hasHeightForWidth())
        self.label_proxy_address.setSizePolicy(sizePolicy)
        self.label_proxy_address.setObjectName("label_proxy_address")
        self.gridLayout_2.addWidget(self.label_proxy_address, 1, 0, 1, 1)
        self.input_lineedit_proxy_password = QtWidgets.QLineEdit(self.groupbox_proxy)
        self.input_lineedit_proxy_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_lineedit_proxy_password.setObjectName("input_lineedit_proxy_password")
        self.gridLayout_2.addWidget(self.input_lineedit_proxy_password, 3, 1, 1, 1)
        self.input_checkbox_use_proxy_from_os = QtWidgets.QCheckBox(self.groupbox_proxy)
        self.input_checkbox_use_proxy_from_os.setObjectName("input_checkbox_use_proxy_from_os")
        self.gridLayout_2.addWidget(self.input_checkbox_use_proxy_from_os, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.groupbox_proxy, 18, 0, 1, 4)
        self.button_box = QtWidgets.QDialogButtonBox(settings_server)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 29, 3, 1, 1)
        self.label_server_type = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_server_type.sizePolicy().hasHeightForWidth())
        self.label_server_type.setSizePolicy(sizePolicy)
        self.label_server_type.setObjectName("label_server_type")
        self.gridLayout.addWidget(self.label_server_type, 1, 0, 1, 1)
        self.label_username = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 6, 0, 1, 1)
        self.label_monitor_url = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monitor_url.sizePolicy().hasHeightForWidth())
        self.label_monitor_url.setSizePolicy(sizePolicy)
        self.label_monitor_url.setObjectName("label_monitor_url")
        self.gridLayout.addWidget(self.label_monitor_url, 4, 0, 1, 1)
        self.input_lineedit_name = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_name.setObjectName("input_lineedit_name")
        self.gridLayout.addWidget(self.input_lineedit_name, 3, 2, 1, 2)
        self.label_monitor_cgi_url = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monitor_cgi_url.sizePolicy().hasHeightForWidth())
        self.label_monitor_cgi_url.setSizePolicy(sizePolicy)
        self.label_monitor_cgi_url.setObjectName("label_monitor_cgi_url")
        self.gridLayout.addWidget(self.label_monitor_cgi_url, 5, 0, 1, 1)
        self.input_checkbox_enabled = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_enabled.setObjectName("input_checkbox_enabled")
        self.gridLayout.addWidget(self.input_checkbox_enabled, 0, 0, 1, 4)
        self.input_checkbox_save_password = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_save_password.setObjectName("input_checkbox_save_password")
        self.gridLayout.addWidget(self.input_checkbox_save_password, 8, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 26, 0, 1, 4)
        self.input_checkbox_show_options = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_show_options.setObjectName("input_checkbox_show_options")
        self.gridLayout.addWidget(self.input_checkbox_show_options, 27, 0, 1, 4)
        self.groupbox_options = QtWidgets.QGroupBox(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_options.sizePolicy().hasHeightForWidth())
        self.groupbox_options.setSizePolicy(sizePolicy)
        self.groupbox_options.setObjectName("groupbox_options")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupbox_options)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 5, 3, 1, 1)
        self.input_checkbox_use_autologin = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_use_autologin.setObjectName("input_checkbox_use_autologin")
        self.gridLayout_3.addWidget(self.input_checkbox_use_autologin, 7, 1, 1, 3)
        self.input_lineedit_map_to_servicename = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_map_to_servicename.setObjectName("input_lineedit_map_to_servicename")
        self.gridLayout_3.addWidget(self.input_lineedit_map_to_servicename, 14, 2, 1, 2)
        self.input_lineedit_monitor_site = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_monitor_site.setObjectName("input_lineedit_monitor_site")
        self.gridLayout_3.addWidget(self.input_lineedit_monitor_site, 8, 2, 1, 1)
        self.label_autologin_key = QtWidgets.QLabel(self.groupbox_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_autologin_key.sizePolicy().hasHeightForWidth())
        self.label_autologin_key.setSizePolicy(sizePolicy)
        self.label_autologin_key.setObjectName("label_autologin_key")
        self.gridLayout_3.addWidget(self.label_autologin_key, 9, 1, 1, 1)
        self.input_lineedit_service_filter = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_service_filter.setText("")
        self.input_lineedit_service_filter.setObjectName("input_lineedit_service_filter")
        self.gridLayout_3.addWidget(self.input_lineedit_service_filter, 11, 2, 1, 2)
        self.label_map_to_status_information = QtWidgets.QLabel(self.groupbox_options)
        self.label_map_to_status_information.setObjectName("label_map_to_status_information")
        self.gridLayout_3.addWidget(self.label_map_to_status_information, 15, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_lineedit_custom_cert_ca_file = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_custom_cert_ca_file.setObjectName("input_lineedit_custom_cert_ca_file")
        self.horizontalLayout.addWidget(self.input_lineedit_custom_cert_ca_file)
        self.button_choose_custom_cert_ca_file = QtWidgets.QPushButton(self.groupbox_options)
        self.button_choose_custom_cert_ca_file.setObjectName("button_choose_custom_cert_ca_file")
        self.horizontalLayout.addWidget(self.button_choose_custom_cert_ca_file)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 2, 1, 2)
        self.groupbox_checkmk_views = QtWidgets.QGroupBox(self.groupbox_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_checkmk_views.sizePolicy().hasHeightForWidth())
        self.groupbox_checkmk_views.setSizePolicy(sizePolicy)
        self.groupbox_checkmk_views.setObjectName("groupbox_checkmk_views")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupbox_checkmk_views)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_checkmk_view_hosts = QtWidgets.QLabel(self.groupbox_checkmk_views)
        self.label_checkmk_view_hosts.setObjectName("label_checkmk_view_hosts")
        self.gridLayout_4.addWidget(self.label_checkmk_view_hosts, 0, 0, 1, 1)
        self.label_checkmk_view_services = QtWidgets.QLabel(self.groupbox_checkmk_views)
        self.label_checkmk_view_services.setObjectName("label_checkmk_view_services")
        self.gridLayout_4.addWidget(self.label_checkmk_view_services, 1, 0, 1, 1)
        self.input_lineedit_checkmk_view_services = QtWidgets.QLineEdit(self.groupbox_checkmk_views)
        self.input_lineedit_checkmk_view_services.setObjectName("input_lineedit_checkmk_view_services")
        self.gridLayout_4.addWidget(self.input_lineedit_checkmk_view_services, 1, 1, 1, 1)
        self.input_lineedit_checkmk_view_hosts = QtWidgets.QLineEdit(self.groupbox_checkmk_views)
        self.input_lineedit_checkmk_view_hosts.setObjectName("input_lineedit_checkmk_view_hosts")
        self.gridLayout_4.addWidget(self.input_lineedit_checkmk_view_hosts, 0, 1, 1, 1)
        self.button_checkmk_view_hosts_reset = QtWidgets.QPushButton(self.groupbox_checkmk_views)
        self.button_checkmk_view_hosts_reset.setObjectName("button_checkmk_view_hosts_reset")
        self.gridLayout_4.addWidget(self.button_checkmk_view_hosts_reset, 0, 2, 1, 1)
        self.button_checkmk_view_services_reset = QtWidgets.QPushButton(self.groupbox_checkmk_views)
        self.button_checkmk_view_services_reset.setObjectName("button_checkmk_view_services_reset")
        self.gridLayout_4.addWidget(self.button_checkmk_view_services_reset, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupbox_checkmk_views, 21, 1, 1, 3)
        self.label_timeout = QtWidgets.QLabel(self.groupbox_options)
        self.label_timeout.setObjectName("label_timeout")
        self.gridLayout_3.addWidget(self.label_timeout, 6, 1, 1, 1)
        self.horizontalLayout_timeout_seconds = QtWidgets.QHBoxLayout()
        self.horizontalLayout_timeout_seconds.setSpacing(5)
        self.horizontalLayout_timeout_seconds.setObjectName("horizontalLayout_timeout_seconds")
        self.input_spinbox_timeout = QtWidgets.QSpinBox(self.groupbox_options)
        self.input_spinbox_timeout.setObjectName("input_spinbox_timeout")
        self.horizontalLayout_timeout_seconds.addWidget(self.input_spinbox_timeout)
        self.label_timeout_sec = QtWidgets.QLabel(self.groupbox_options)
        self.label_timeout_sec.setObjectName("label_timeout_sec")
        self.horizontalLayout_timeout_seconds.addWidget(self.label_timeout_sec)
        self.gridLayout_3.addLayout(self.horizontalLayout_timeout_seconds, 6, 2, 1, 1)
        self.label_auth_type = QtWidgets.QLabel(self.groupbox_options)
        self.label_auth_type.setObjectName("label_auth_type")
        self.gridLayout_3.addWidget(self.label_auth_type, 5, 1, 1, 1)
        self.input_combobox_authentication = QtWidgets.QComboBox(self.groupbox_options)
        self.input_combobox_authentication.setObjectName("input_combobox_authentication")
        self.gridLayout_3.addWidget(self.input_combobox_authentication, 5, 2, 1, 1)
        self.input_checkbox_custom_cert_use = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_custom_cert_use.setObjectName("input_checkbox_custom_cert_use")
        self.gridLayout_3.addWidget(self.input_checkbox_custom_cert_use, 1, 1, 1, 2)
        self.input_checkbox_no_cookie_auth = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_no_cookie_auth.setObjectName("input_checkbox_no_cookie_auth")
        self.gridLayout_3.addWidget(self.input_checkbox_no_cookie_auth, 16, 1, 1, 3)
        self.input_checkbox_force_authuser = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_force_authuser.setObjectName("input_checkbox_force_authuser")
        self.gridLayout_3.addWidget(self.input_checkbox_force_authuser, 20, 1, 1, 3)
        self.input_lineedit_map_to_hostname = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_map_to_hostname.setObjectName("input_lineedit_map_to_hostname")
        self.gridLayout_3.addWidget(self.input_lineedit_map_to_hostname, 13, 2, 1, 2)
        self.input_lineedit_host_filter = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_host_filter.setText("")
        self.input_lineedit_host_filter.setObjectName("input_lineedit_host_filter")
        self.gridLayout_3.addWidget(self.input_lineedit_host_filter, 10, 2, 1, 2)
        self.input_lineedit_alertmanager_filter = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_alertmanager_filter.setObjectName("input_lineedit_alertmanager_filter")
        self.gridLayout_3.addWidget(self.input_lineedit_alertmanager_filter, 12, 2, 1, 2)
        self.input_checkbox_use_display_name_service = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_use_display_name_service.setObjectName("input_checkbox_use_display_name_service")
        self.gridLayout_3.addWidget(self.input_checkbox_use_display_name_service, 18, 1, 1, 3)
        self.input_checkbox_ignore_cert = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_ignore_cert.setObjectName("input_checkbox_ignore_cert")
        self.gridLayout_3.addWidget(self.input_checkbox_ignore_cert, 0, 1, 1, 3)
        self.label_host_filter = QtWidgets.QLabel(self.groupbox_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_host_filter.sizePolicy().hasHeightForWidth())
        self.label_host_filter.setSizePolicy(sizePolicy)
        self.label_host_filter.setObjectName("label_host_filter")
        self.gridLayout_3.addWidget(self.label_host_filter, 10, 1, 1, 1)
        self.input_lineedit_map_to_status_information = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_map_to_status_information.setObjectName("input_lineedit_map_to_status_information")
        self.gridLayout_3.addWidget(self.input_lineedit_map_to_status_information, 15, 2, 1, 2)
        self.label_monitor_site = QtWidgets.QLabel(self.groupbox_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monitor_site.sizePolicy().hasHeightForWidth())
        self.label_monitor_site.setSizePolicy(sizePolicy)
        self.label_monitor_site.setObjectName("label_monitor_site")
        self.gridLayout_3.addWidget(self.label_monitor_site, 8, 1, 1, 1)
        self.label_service_filter = QtWidgets.QLabel(self.groupbox_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_service_filter.sizePolicy().hasHeightForWidth())
        self.label_service_filter.setSizePolicy(sizePolicy)
        self.label_service_filter.setObjectName("label_service_filter")
        self.gridLayout_3.addWidget(self.label_service_filter, 11, 1, 1, 1)
        self.input_checkbox_use_description_name_service = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_use_description_name_service.setObjectName("input_checkbox_use_description_name_service")
        self.gridLayout_3.addWidget(self.input_checkbox_use_description_name_service, 19, 1, 1, 3)
        self.label_map_to_hostname = QtWidgets.QLabel(self.groupbox_options)
        self.label_map_to_hostname.setObjectName("label_map_to_hostname")
        self.gridLayout_3.addWidget(self.label_map_to_hostname, 13, 1, 1, 1)
        self.label_custom_ca_file = QtWidgets.QLabel(self.groupbox_options)
        self.label_custom_ca_file.setObjectName("label_custom_ca_file")
        self.gridLayout_3.addWidget(self.label_custom_ca_file, 2, 1, 1, 1)
        self.input_checkbox_use_display_name_host = QtWidgets.QCheckBox(self.groupbox_options)
        self.input_checkbox_use_display_name_host.setObjectName("input_checkbox_use_display_name_host")
        self.gridLayout_3.addWidget(self.input_checkbox_use_display_name_host, 17, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 6, 3, 1, 1)
        self.label_map_to_servicename = QtWidgets.QLabel(self.groupbox_options)
        self.label_map_to_servicename.setObjectName("label_map_to_servicename")
        self.gridLayout_3.addWidget(self.label_map_to_servicename, 14, 1, 1, 1)
        self.input_lineedit_autologin_key = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_autologin_key.setText("")
        self.input_lineedit_autologin_key.setObjectName("input_lineedit_autologin_key")
        self.gridLayout_3.addWidget(self.input_lineedit_autologin_key, 9, 2, 1, 2)
        self.label_alertmanager_filter = QtWidgets.QLabel(self.groupbox_options)
        self.label_alertmanager_filter.setObjectName("label_alertmanager_filter")
        self.gridLayout_3.addWidget(self.label_alertmanager_filter, 12, 1, 1, 1)
        self.label_idp_ecp_endpoint = QtWidgets.QLabel(self.groupbox_options)
        self.label_idp_ecp_endpoint.setObjectName("label_idp_ecp_endpoint")
        self.gridLayout_3.addWidget(self.label_idp_ecp_endpoint, 22, 1, 1, 1)
        self.input_lineedit_idp_ecp_endpoint = QtWidgets.QLineEdit(self.groupbox_options)
        self.input_lineedit_idp_ecp_endpoint.setObjectName("input_lineedit_idp_ecp_endpoint")
        self.gridLayout_3.addWidget(self.input_lineedit_idp_ecp_endpoint, 22, 2, 1, 2)
        self.gridLayout.addWidget(self.groupbox_options, 28, 0, 1, 4)

        self.retranslateUi(settings_server)
        QtCore.QMetaObject.connectSlotsByName(settings_server)
        settings_server.setTabOrder(self.input_checkbox_enabled, self.input_combobox_type)
        settings_server.setTabOrder(self.input_combobox_type, self.input_lineedit_name)
        settings_server.setTabOrder(self.input_lineedit_name, self.input_lineedit_monitor_url)
        settings_server.setTabOrder(self.input_lineedit_monitor_url, self.input_lineedit_monitor_cgi_url)
        settings_server.setTabOrder(self.input_lineedit_monitor_cgi_url, self.input_lineedit_username)
        settings_server.setTabOrder(self.input_lineedit_username, self.input_lineedit_password)
        settings_server.setTabOrder(self.input_lineedit_password, self.input_checkbox_save_password)
        settings_server.setTabOrder(self.input_checkbox_save_password, self.input_checkbox_use_proxy)
        settings_server.setTabOrder(self.input_checkbox_use_proxy, self.input_lineedit_proxy_address)
        settings_server.setTabOrder(self.input_lineedit_proxy_address, self.input_lineedit_proxy_username)
        settings_server.setTabOrder(self.input_lineedit_proxy_username, self.input_lineedit_proxy_password)
        settings_server.setTabOrder(self.input_lineedit_proxy_password, self.input_checkbox_use_proxy_from_os)

    def retranslateUi(self, settings_server):
        _translate = QtCore.QCoreApplication.translate
        settings_server.setWindowTitle(_translate("settings_server", "Dialog"))
        self.label_password.setText(_translate("settings_server", "Password:"))
        self.input_lineedit_monitor_url.setText(_translate("settings_server", "https://monitor-server"))
        self.label_name.setText(_translate("settings_server", "Monitor name:"))
        self.input_lineedit_username.setText(_translate("settings_server", "username"))
        self.input_lineedit_monitor_cgi_url.setText(_translate("settings_server", "https://monitor-server/monitor/cgi-bin"))
        self.input_lineedit_password.setText(_translate("settings_server", "1234567890"))
        self.input_checkbox_use_proxy.setText(_translate("settings_server", "Use proxy"))
        self.groupbox_proxy.setTitle(_translate("settings_server", "Proxy:"))
        self.label_proxy_password.setText(_translate("settings_server", "Proxy password:"))
        self.label_proxy_username.setText(_translate("settings_server", "Proxy username:"))
        self.input_lineedit_proxy_username.setText(_translate("settings_server", "proxyusername"))
        self.input_lineedit_proxy_address.setText(_translate("settings_server", "http://proxy:port/"))
        self.label_proxy_address.setText(_translate("settings_server", "Proxy address:"))
        self.input_lineedit_proxy_password.setText(_translate("settings_server", "1234567890"))
        self.input_checkbox_use_proxy_from_os.setText(_translate("settings_server", "Use proxy from OS"))
        self.label_server_type.setText(_translate("settings_server", "Monitor type:"))
        self.label_username.setText(_translate("settings_server", "Username:"))
        self.label_monitor_url.setText(_translate("settings_server", "Monitor URL:"))
        self.input_lineedit_name.setText(_translate("settings_server", "Monitor server"))
        self.label_monitor_cgi_url.setText(_translate("settings_server", "Monitor CGI URL:"))
        self.input_checkbox_enabled.setText(_translate("settings_server", "Enabled"))
        self.input_checkbox_save_password.setText(_translate("settings_server", "Save password"))
        self.input_checkbox_show_options.setText(_translate("settings_server", "Show more options"))
        self.groupbox_options.setTitle(_translate("settings_server", "Options:"))
        self.input_checkbox_use_autologin.setText(_translate("settings_server", "Use autologin"))
        self.input_lineedit_monitor_site.setText(_translate("settings_server", "Site 1"))
        self.label_autologin_key.setText(_translate("settings_server", "Autologin Key:"))
        self.label_map_to_status_information.setText(_translate("settings_server", "Map to status_information:"))
        self.button_choose_custom_cert_ca_file.setText(_translate("settings_server", "Choose file..."))
        self.groupbox_checkmk_views.setTitle(_translate("settings_server", "Views:"))
        self.label_checkmk_view_hosts.setText(_translate("settings_server", "Hosts:"))
        self.label_checkmk_view_services.setText(_translate("settings_server", "Services:"))
        self.button_checkmk_view_hosts_reset.setText(_translate("settings_server", "Reset"))
        self.button_checkmk_view_services_reset.setText(_translate("settings_server", "Reset"))
        self.label_timeout.setText(_translate("settings_server", "Timeout:"))
        self.label_timeout_sec.setText(_translate("settings_server", "seconds"))
        self.label_auth_type.setText(_translate("settings_server", "Authentication:"))
        self.input_checkbox_custom_cert_use.setText(_translate("settings_server", "Use custom CA file"))
        self.input_checkbox_no_cookie_auth.setText(_translate("settings_server", "Do not use cookie authentication"))
        self.input_checkbox_force_authuser.setText(_translate("settings_server", "Only show permitted hosts for \"see all\" users (1.4.0i1 or newer)"))
        self.input_checkbox_use_display_name_service.setText(_translate("settings_server", "Use display name as service name"))
        self.input_checkbox_ignore_cert.setText(_translate("settings_server", "Ignore SSL/TLS certificate"))
        self.label_host_filter.setText(_translate("settings_server", "Host filter:"))
        self.label_monitor_site.setText(_translate("settings_server", "Monitor Site:"))
        self.label_service_filter.setText(_translate("settings_server", "Service filter:"))
        self.input_checkbox_use_description_name_service.setText(_translate("settings_server", "Use description as service name"))
        self.label_map_to_hostname.setText(_translate("settings_server", "Map to hostname:"))
        self.label_custom_ca_file.setText(_translate("settings_server", "Custom CA file: "))
        self.input_checkbox_use_display_name_host.setText(_translate("settings_server", "Use display name as host name"))
        self.label_map_to_servicename.setText(_translate("settings_server", "Map to servicename:"))
        self.label_alertmanager_filter.setText(_translate("settings_server", "Filter:"))
        self.label_idp_ecp_endpoint.setText(_translate("settings_server", "IdP ECP endpoint URL"))
