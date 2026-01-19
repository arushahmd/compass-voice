# app/state_machine/state_router.py

from typing import Dict, Set

from app.state_machine.conversation_state import ConversationState
from app.state_machine.route_result import RouteResult
from app.nlu.intent import Intent


class StateRouter:
    """
    Authoritative router that decides whether a detected intent
    is allowed to execute in the current conversation state.
    """

    def __init__(self) -> None:
        self._allowed_intents: Dict[ConversationState, Set[Intent]] = {
            ConversationState.GREETING: {
                Intent.CONFIRM,
                Intent.UNKNOWN,
            },

            ConversationState.IDLE: {
                Intent.ADD_ITEM,
                Intent.MODIFY_ITEM,
                Intent.REMOVE_ITEM,
                Intent.SHOW_MENU,
                Intent.SHOW_CART,
                Intent.SHOW_TOTAL,
            },

            ConversationState.WAITING_FOR_SIDE: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
                Intent.UNKNOWN,   # side matching happens here
            },

            ConversationState.WAITING_FOR_MODIFIER: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
                Intent.UNKNOWN,
            },

            ConversationState.WAITING_FOR_SIZE: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
                Intent.UNKNOWN,
            },

            ConversationState.WAITING_FOR_QUANTITY: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
                Intent.UNKNOWN,
            },

            ConversationState.CONFIRMING: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
            },

            ConversationState.MODIFYING_ITEM: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
                Intent.UNKNOWN,
            },

            ConversationState.REMOVING_ITEM: {
                Intent.CONFIRM,
                Intent.DENY,
                Intent.CANCEL,
            },

            ConversationState.SHOWING_CART: {
                Intent.CONFIRM,
                Intent.CANCEL,
            },

            ConversationState.SHOWING_TOTAL: {
                Intent.CONFIRM,
                Intent.CANCEL,
            },

            ConversationState.CANCELLATION_CONFIRMATION: {
                Intent.CONFIRM,
                Intent.DENY,
            },

            ConversationState.ERROR_RECOVERY: {
                Intent.CONFIRM,
                Intent.CANCEL,
                Intent.UNKNOWN,
            },
        }

<<<<<<< Updated upstream
    def route(
        self,
        state: ConversationState,
        intent: Intent,
    ) -> RouteResult:
        """
        Determines whether the given intent is allowed in the current state.
        """

        allowed_intents = self._allowed_intents.get(state, set())

=======
    def route(self, state: ConversationState, intent_result: IntentResult) -> RouteResult:
        intent = intent_result.intent

        # 🔹 ADD ITEM always starts add-item task
        if state == ConversationState.IDLE and intent == Intent.ADD_ITEM:
            return RouteResult(
                allowed=True,
                handler_name="add_item_handler",
            )

        # 🔹 END ADDING / START ORDER
        if state == ConversationState.IDLE and intent in {
            Intent.END_ADDING,
            Intent.START_ORDER,
        }:
            return RouteResult(
                allowed=True,
                handler_name="start_order_handler",
            )

        # 🔹 Payment flow
        if state == ConversationState.WAITING_FOR_PAYMENT:
            return RouteResult(
                allowed=True,
                handler_name="waiting_for_payment_handler",
            )

        # 🔒 Default state-based routing
        allowed_intents = self._allowed_intents.get(state, set())
>>>>>>> Stashed changes
        if intent in allowed_intents:
            return RouteResult(
                allowed=True,
                handler_name=f"{state.name.lower()}_handler",
            )

<<<<<<< Updated upstream
        # Cancellation override (global escape hatch)
=======
>>>>>>> Stashed changes
        if intent == Intent.CANCEL and state != ConversationState.IDLE:
            return RouteResult(
                allowed=True,
                handler_name="cancel_handler",
            )

<<<<<<< Updated upstream
        return RouteResult(
            allowed=False,
            reason=(
                f"Intent {intent.name} not allowed in state {state.name}. "
                "Please complete or cancel the current action first."
            ),
        )
=======
        return RouteResult(allowed=False)


>>>>>>> Stashed changes
