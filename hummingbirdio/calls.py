import asyncio

class HummingBirdCalls:  # Cacaw!
    def __init__(self, hummingbird):
        self.request = hummingbird.request

    # Standard API starts here vv https://developer.twitter.com/en/docs/api-reference-index

    # GET section

    async def get_settings(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings
        """
        return await self.request('account/settings.json', params=params)

    async def verify_credentials(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials
        """
        return await self.request('account/verify_credentials.json', params=params)

    async def rate_limit_status(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials
        """
        return await self.request('application/rate_limit_status.json', params=params)

    async def blocked_ids(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids
        """
        return await self.request('blocks/ids.json', params=params)

    async def block_list(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-blocks-list
        """
        return await self.request('blocks/list.json', params=params)

    async def collections_entries(self, **params):
        """https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/get-collections-entries
        """
        return await self.request('collections/entries.json', params=params)

    async def collections_list(self, **params):
        """https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/get-collections-list
        """
        return await self.request('collections/list.json', params=params)

    async def show_collections(self, **params):
        """https://developer.twitter.com/en/docs/tweets/curate-a-collection/api-reference/get-collections-show
        """
        return await self.request('collections/show.json', params=params)

    async def dm_events_list(self, **params):
        """https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events
        """
        return await self.request('direct_messages/events/list.json', params=params)

    async def dm_events_show(self, **params):
        """https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/get-event
        """
        return await self.request('direct_messages/events/show.json', params=params)

    async def likes_list(self, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-favorites-list
        """
        return await self.request('favorites/list.json', params=params)

    async def follower_ids(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids
        """
        return await self.request('followers/ids.json', params=params)

    async def followers_list(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-list
        """
        return await self.request('followers/list.json', params=params)

    async def following_ids(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids
        """
        return await self.request('friends/ids.json', params=params)

    async def list_following(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-list
        """
        return await self.request('friends/list.json', params=params)

    async def pending_incoming_follows(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-incoming
        """
        return await self.request('friendships/incoming.json', params=params)

    async def lookup_friendships(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup
        """
        return await self.request('friendships/lookup.json', params=params)

    async def following_but_no_retweets(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-no_retweets-ids
        """
        return await self.request('friendships/no_retweets/ids.json', params=params)

    async def pending_outgoing_follows(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-outgoing
        """
        return await self.request('friendships/outgoing.json', params=params)

    async def show_relationship(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show
        """
        return await self.request('friendships/show.json', params=params)

    async def get_geo_info(self, place_id=None, **params):
        """https://developer.twitter.com/en/docs/geo/place-information/api-reference/get-geo-id-place_id
        """
        return await self.request('geo/id/{}.json'.format(place_id), params=params)

    async def reverse_geocode(self, **params):
        """https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode
        """
        return await self.request('geo/reverse_geocode.json', params=params)

    async def geo_search(self, **params):
        """https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search
        """
        return await self.request('geo/search.json', params=params)

    async def help_config(self, **params):
        """https://developer.twitter.com/en/docs/developer-utilities/configuration/api-reference/get-help-configuration
        """
        return await self.request('help/configuration.json', params=params)

    async def help_lang(self, **params):
        """https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages
        """
        return await self.request('help/languages.json', params=params)

    async def help_privacy(self, **params):
        """https://developer.twitter.com/en/docs/developer-utilities/privacy-policy/api-reference/get-help-privacy
        """
        return await self.request('help/privacy.json', params=params)

    async def help_tos(self, **params):
        """https://developer.twitter.com/en/docs/developer-utilities/terms-of-service/api-reference/get-help-tos
        """
        return await self.request('help/tos.json', params=params)

    async def list_lists(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-list
        """
        return await self.request('lists/list.json', params=params)

    async def list_members(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-members
        """
        return await self.request('lists/members.json', params=params)

    async def check_list_for_member(self, **params):  # 404?
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-members-show
        """
        return await self.request('lists/members/show.json', params=params)

    async def show_list_memberships(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships
        """
        return await self.request('lists/memberships.json', params=params)

    async def list_ownerships(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-ownerships
        """
        return await self.request('lists/ownerships.json', params=params)

    async def show_list_details(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-show
        """
        return await self.request('lists/show.json', params=params)

    async def show_list_member_statuses(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses
        """
        return await self.request('lists/statuses.json', params=params)

    async def show_list_subscribers(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers
        """
        return await self.request('lists/subscribers.json', params=params)

    async def check_if_list_subscriber(self, **params):  # 404?
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers-show
        """
        return await self.request('lists/subscribers/show.json', params=params)

    async def show_users_list_subscriptions(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-subscriptions
        """
        return await self.request('lists/subscriptions.json', params=params)

    async def check_media_upload_status(self, **params):  # Untested
        """https://developer.twitter.com/en/docs/media/upload-media/api-reference/get-media-upload-status
        """
        return await self.request('https://upload.twitter.com/1.1/media/upload.json', params=params)

    async def muted_ids(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids
        """
        return await self.request('mutes/users/ids.json', params=params)

    async def muted_users(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list
        """
        return await self.request('mutes/users/list.json', params=params)

    async def saved_search_list(self, **params):
        """https://developer.twitter.com/en/docs/tweets/search/api-reference/get-saved_searches-list
        """  # Broken link
        return await self.request('saved_searches/list.json', params=params)

    async def saved_search_show(self, user_id=None, **params):  # 403?
        """https://developer.twitter.com/en/docs/tweets/search/api-reference/get-saved_searches-show-id
        """  # Broken link
        return await self.request('saved_searches/show/{}'.format(user_id), params=params)

    async def search_tweets(self, **params):
        """https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
        """
        return await self.request('search/tweets.json', params=params)

    async def timeline(self, **params):
        """https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline
        """
        return await self.request('statuses/home_timeline.json', params=params)

    async def statuses_lookup(self, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup
        """
        return await self.request('statuses/lookup.json', params=params)

    async def mentions_timeline(self, **params):
        """https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-mentions_timeline
        """
        return await self.request('statuses/mentions_timeline.json', params=params)

    async def statuses_oembed(self, **params):  # URL param conflicts with aioauth-client
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed
        """
        return await self.request('https://publish.twitter.com/oembed', params=params)

    async def retweeters_of_tweet(self, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids
        """
        return await self.request('statuses/retweeters/ids.json', params=params)

    async def retweeters_of_me(self, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweets_of_me
        """
        return await self.request('statuses/retweets_of_me.json', params=params)

    async def show_tweet_by_id(self, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id
        """
        return await self.request('statuses/show.json', params=params)

    async def user_timeline(self, **params):
        """https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
        """
        return await self.request('statuses/user_timeline.json', params=params)

    async def trend_locations(self, **params):
        """https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available
        """
        return await self.request('trends/available.json', params=params)

    async def closest_trends(self, **params):
        """https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-closest
        """
        return await self.request('trends/closest.json', params=params)

    async def trends_by_place(self, **params):
        """https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place
        """
        return await self.request('trends/place.json', params=params)

    async def lookup_users(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup
        """
        return await self.request('users/lookup.json', params=params)

    async def user_profile_banner(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner
        """
        return await self.request('users/profile_banner.json', params=params)

    async def search_for_users(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-search
        """
        return await self.request('users/search.json', params=params)

    async def show_user_info(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show
        """
        return await self.request('users/show.json', params=params)

    async def suggested_users(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-suggestions
        """
        return await self.request('users/suggestions.json', params=params)

    async def suggested_users_by_slug(self, slug=None, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-suggestions-slug
        """
        return await self.request('users/suggestions/{}.json'.format(slug), params=params)

    async def suggested_users_by_slug_with_recent_tweet(self, slug=None, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-suggestions-slug-members
        """
        return await self.request('users/suggestions/{}/members.json'.format(slug), params=params)

    # POST section

    async def remove_profile_banner(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-remove_profile_banner
        """
        return await self.request('account/remove_profile_banner.json', method='POST', params=params)

    async def update_settings(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-settings
        """
        return await self.request('account/settings.json', method='POST', params=params)

    async def update_profile(self, **params):  # 401?
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile
        """
        return await self.request('account/update_profile.json', method='POST', params=params)

    async def update_profile_background_image(self, **params):  # Unreliable/broken
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_background_image
        """
        return await self.request('account/update_profile_background_image.json', method='POST', params=params)

    async def update_profile_banner(self, **params):  # Unreliable/broken
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner
        """
        return await self.request('account/update_profile_banner.json', method='POST', params=params)

    async def update_profile_image(self, **params):  # Unreliable/broken
        """https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image
        """
        return await self.request('account/update_profile_image.json', method='POST', params=params)

    async def mute_user(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create
        """
        return await self.request('mutes/users/create.json', method='POST', params=params)

    async def unmute_user(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy
        """
        return await self.request('mutes/users/destroy.json', method='POST', params=params)

    async def save_search(self, **params):
        """https://developer.twitter.com/en/docs/tweets/search/api-reference/post-saved_searches-create
        """  # Broken link
        return await self.request('saved_searches/create.json', method='POST', params=params)

    async def delete_search(self, id=None, **params):
        """"https://developer.twitter.com/en/docs/tweets/search/api-reference/post-saved_searches-destroy-id
        """  # Broken link
        return await self.request('saved_searches/destroy/{}.json'.format(id), method='POST', params=params)

    async def delete_tweet(self, id=None, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-destroy-id
        """
        return await self.request('statuses/destroy/{}.json'.format(id), method='POST', params=params)

    async def retweet(self, id=None, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id
        """
        return await self.request('statuses/retweet/{}.json'.format(id), method='POST', params=params)

    async def unretweet(self, id=None, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-unretweet-id
        """
        return await self.request('statuses/unretweet/{}.json'.format(id), method='POST', params=params)

    async def tweet(self, **params):
        """https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update
        """
        return await self.request('statuses/update.json', method='POST', params=params)

    async def report_spam(self, **params):
        """https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-users-report_spam
        """
        return await self.request('users/report_spam.json', method='POST', params=params)

    # DELETE section

    async def delete_welcome_dm(self, **params):  # Untested
        """https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/delete-welcome-message
        """
        return await self.request('direct_messages/welcome_messages/destroy.json', method='DELETE', params=params)

    async def delete_welcome_rules_dm(self, **params):  # Untested
        """https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/delete-welcome-message-rule
        """
        return await self.request('direct_messages/welcome_messages/rules/destroy.json', method='DELETE', params=params)


class HummingBirdStreamCalls:
    def __init__(self, hummingbird):
        self.request = hummingbird.request
        self.queue = asyncio.Queue()

    async def filter(self, **params):
        """https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter
        """
        return await self.request('https://stream.twitter.com/1.1/statuses/filter.json',
                                  method='POST', stream_queue=self.queue, params=params)

    async def sample(self, **params):
        """https://developer.twitter.com/en/docs/tweets/sample-realtime/api-reference/get-statuses-sample
        """
        return await self.request('https://stream.twitter.com/1.1/statuses/sample.json',
                                  stream_queue=self.queue, params=params)
