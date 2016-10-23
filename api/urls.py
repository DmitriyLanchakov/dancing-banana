from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_client_info$', "api.views.get_client_info"),
    url(r'^update_client_info$', "api.views.update_client_info"),
    url(r'^get_clients$', "api.views.get_clients"),
    url(r'^sms_received$', "api.views.sms_received"),

    url(r'^get_coc_info$', "api.views.get_coc_info"),
    url(r'^get_cocs$', "api.views.get_cocs"),

    url(r'^ask_for_help$', "api.views.ask_for_help"),
    url(r'^log_note$', "api.views.log_note"),
    url(r'^grant_bed$', "api.views.grant_bed"),
    url(r'^submit_referral$', "api.views.submit_referral"),

    url(r'^$', "api.views.load_frontend")
)
