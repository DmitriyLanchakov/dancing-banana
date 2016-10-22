'use-strict'

// API Routes:

// client factory
// client_search (client_name, phone_number) -> list of client matches
// update_client_info (profile_info, optional client_id) -> success
// get_client_info (client_id) -> client info/event info for client
// log_note (client_id, coc_id) -> success


// coc factory
// get_coc_info (coc_location) -> # of beds, # available, pending requests/referrals
// grant_bed (client_id, coc_id) -> success (updates # available on front end)
// get_cocs (client_id, location, coc_type) -> coc list (for admin page and for client page) 
// ask_for_help () -> coc id/ name/ phone

// referral factory
// submit_referral (client_id, to_coc_id, from_coc_id, comments) -> success

// entry point is index.js????