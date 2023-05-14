from django.http import HttpResponse


class StripeWH_Handler:
    '''
    Handles Stripe webhooks
    '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        '''
        Handle generic/unexpected/unknown webhook event
        '''
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
