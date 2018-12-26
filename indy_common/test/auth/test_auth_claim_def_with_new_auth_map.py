from indy_common.authorize.auth_actions import AuthActionAdd, AuthActionEdit

from indy_common.constants import CLAIM_DEF


def test_claim_def_adding(write_request_validation, req, is_owner):
    authorized = req.identifier in ("trustee_identifier", "steward_identifier", "trust_anchor_identifier")
    assert authorized == write_request_validation(req,
                                                  [AuthActionAdd(txn_type=CLAIM_DEF,
                                                                 field='some_field',
                                                                 value='some_value',
                                                                 is_owner=is_owner)])


def test_claim_def_editing(write_request_validation, req, is_owner):
    authorized = is_owner
    assert authorized == write_request_validation(req,
                                                  [AuthActionEdit(txn_type=CLAIM_DEF,
                                                                  field='some_field',
                                                                  old_value='old_value',
                                                                  new_value='new_value',
                                                                  is_owner=is_owner)])
