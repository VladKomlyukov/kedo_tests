
employee_personal_info_schema_v3: dict = {
    "type": "object",
    "properties": {
        "Id": {
            "type": "string"
        },
        "FirstName": {
            "type": "string"
        },
        "LastName": {
            "type": "string"
        },
        "MiddleName": {
            "type": ["string", "null"]
        },
        "BirthDate": {
            "type": "string"
        },
        "Gender": {
            "type": "string"
        },
        "Snils": {
            "type": "string"
        },
        "Inn": {
            "type": "string"
        },
        "PhoneNumber": {
            "type": "string"
        },
        "Email": {
            "type": ["string", "null"]
        },
        "EmployeeWorkplaceId": {
            "type": "string"
        },
        "Tenant": {
            "type": "object",
            "properties": {
                "Id": {
                    "type": "string"
                },
                "Fullname": {
                    "type": "string"
                },
                "Shortname": {
                    "type": "string"
                },
                "WorkBegan": {
                    "type": "string"
                },
                "WorkEnded": {
                    "type": ["string", "null"]
                }
            },
            "required": [
                "Id",
                "Fullname",
                "Shortname",
                "WorkBegan"
            ]
        },
        "PersonalCode": {
            "type": "string"
        },
        "AccessRole": {
            "type": "string"
        }
    },
    "required": [
        "Id",
        "FirstName",
        "LastName",
        "BirthDate",
        "Gender",
        "Snils",
        "Inn",
        "PhoneNumber",
        "EmployeeWorkplaceId",
        "Tenant",
        "PersonalCode",
        "AccessRole"
    ]
}

employees_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Id": {
                "type": "string"
            },
            "UserId": {
                "type": "string"
            },
            "FirstName": {
                "type": "string"
            },
            "LastName": {
                "type": "string"
            },
            "MiddleName": {
                "type": ["string", "null"]
            },
            "BirthDate": {
                "type": "string"
            },
            "Gender": {
                "type": "string"
            },
            "EmployeeWorkplaceId": {
                "type": ["string", "null"]
            },
            "SubdivisionName": {
                "type": ["string", "null"]
            },
            "JobTitleName": {
                "type": ["string", "null"]
            },
            "PhoneNumber": {
                "type": "string"
            },
            "Email": {
                "type": ["string", "null"]
            },
            "IsActive": {
                "type": "boolean"
            },
            "Status": {
                "type": "string"
            }
        },
        "required": [
            "Id",
            "UserId",
            "FirstName",
            "LastName",
            "MiddleName",
            "BirthDate",
            "Gender",
            "PhoneNumber",
            "IsActive",
            "Status"
        ]
    }
}

employee_by_id_schema_schema_v3: dict = {
    "type": "object",
    "properties": {
        "UserId": {
            "type": "string"
        },
        "Tenant": {
            "type": "object",
            "properties": {
                "Id": {
                    "type": "string"
                },
                "Fullname": {
                    "type": "string"
                },
                "Shortname": {
                    "type": "string"
                },
                "WorkBegan": {
                    "type": "string"
                },
                "WorkEnded": {
                    "type": "null"
                }
            },
            "required": [
                "Id",
                "Fullname",
                "Shortname",
                "WorkBegan"
            ]
        },
        "FirstName": {
            "type": "string"
        },
        "LastName": {
            "type": "string"
        },
        "MiddleName": {
            "type": ["string", "null"]
        },
        "BirthDate": {
            "type": "string"
        },
        "Gender": {
            "type": "string"
        },
        "PersonalInfo": {
            "type": "object",
            "properties": {
                "PassportSerial": {
                    "type": "string"
                },
                "PassportNumber": {
                    "type": "string"
                },
                "PassportIssuer": {
                    "type": "string"
                },
                "BirthAddress": {
                    "type": "string"
                },
                "RegistrationAddress": {
                    "type": "string"
                },
                "PlaceOfResidence": {
                    "type": "string"
                },
                "IssuerSubdivisionCode": {
                    "type": "string"
                },
                "DateOfIssued": {
                    "type": "string"
                },
                "DateOfExpiration": {
                    "type": ["string", "null"]
                },
                "CountryCode": {
                    "type": "string"
                },
                "CountryName": {
                    "type": "string"
                },
                "IsResident": {
                    "type": "boolean"
                },
                "Snils": {
                    "type": "string"
                },
                "Inn": {
                    "type": "string"
                }
            },
            "required": [
                "PassportSerial",
                "PassportNumber",
                "PassportIssuer",
                "BirthAddress",
                "RegistrationAddress",
                "PlaceOfResidence",
                "IssuerSubdivisionCode",
                "DateOfIssued",
                "CountryCode",
                "CountryName",
                "IsResident",
                "Snils",
                "Inn"
            ]
        },
        "Contacts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "PhoneNumber": {
                        "type": "string"
                    },
                    "Email": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "Id",
                    "PhoneNumber"
                ]
            }
        },
        "EmployeeWorkplaces": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["string", "null"]
                    },
                    "Subdivision": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "type": "string"
                            },
                            "Name": {
                                "type": "string"
                            },
                            "Tenant": {
                                "type": ["string", "null"]
                            }
                        },
                        "required": [
                            "Id",
                            "Name"
                        ]
                    },
                    "JobTitle": {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "Id": {
                                        "type": "string"
                                    },
                                    "Name": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "Id",
                                    "Name"
                                ]
                            },
                            {
                                "type": ["string", "null"]
                            }
                        ]
                    },
                    "IsActive": {
                        "type": "boolean"
                    },
                    "PersonalCode": {
                        "type": "string"
                    },
                    "IsDeleted": {
                        "type": "boolean"
                    },
                    "DeleterId": {
                        "type": ["string", "null"]
                    },
                    "DeletionTime": {
                        "type": ["string", "null"]
                    },
                    "LastModificationTime": {
                        "type": ["string", "null"]
                    },
                    "LastModifierId": {
                        "type": ["string", "null"]
                    },
                    "CreationTime": {
                        "type": "string"
                    },
                    "CreatorId": {
                        "type": ["string", "null"]
                    },
                    "Id": {
                        "type": "string"
                    }
                },
                "required": [
                    "WorkBegan",
                    "Subdivision",
                    "IsActive",
                    "PersonalCode",
                    "IsDeleted",
                    "CreationTime",
                    "Id"
                ]
            }
        },
        "Status": {
            "type": "string"
        },
        "CreationTime": {
            "type": "string"
        },
        "AvatarUrl": {
            "type": ["string", "null"]
        }
    },
    "required": [
        "UserId",
        "Tenant",
        "FirstName",
        "LastName",
        "BirthDate",
        "Gender",
        "PersonalInfo",
        "Contacts",
        "EmployeeWorkplaces",
        "Status",
        "CreationTime"
    ]
}

employee_by_id_schema_v3_not_resident: dict = {
    "type": "object",
    "properties": {
        "UserId": {
            "type": "string"
        },
        "Tenant": {
            "type": "object",
            "properties": {
                "Id": {
                    "type": "string"
                },
                "Fullname": {
                    "type": "string"
                },
                "Shortname": {
                    "type": "string"
                },
                "WorkBegan": {
                    "type": "string"
                },
                "WorkEnded": {
                    "type": ["string", "null"]
                }
            },
            "required": [
                "Id",
                "Fullname",
                "Shortname",
                "WorkBegan"
            ]
        },
        "FirstName": {
            "type": "string"
        },
        "LastName": {
            "type": "string"
        },
        "MiddleName": {
            "type": "string"
        },
        "BirthDate": {
            "type": "string"
        },
        "Gender": {
            "type": "string"
        },
        "PersonalInfo": {
            "type": "object",
            "properties": {
                "PassportSerial": {
                    "type": ["string", "null"]
                },
                "PassportNumber": {
                    "type": "string"
                },
                "PassportIssuer": {
                    "type": ["string", "null"]
                },
                "BirthAddress": {
                    "type": "string"
                },
                "RegistrationAddress": {
                    "type": "string"
                },
                "PlaceOfResidence": {
                    "type": ["string", "null"]
                },
                "IssuerSubdivisionCode": {
                    "type": ["string", "null"]
                },
                "DateOfIssued": {
                    "type": "string"
                },
                "DateOfExpiration": {
                    "type": "string"
                },
                "CountryCode": {
                    "type": "string"
                },
                "CountryName": {
                    "type": "string"
                },
                "IsResident": {
                    "type": "boolean"
                },
                "Snils": {
                    "type": "string"
                },
                "Inn": {
                    "type": "string"
                }
            },
            "required": [
                "PassportNumber",
                "BirthAddress",
                "RegistrationAddress",
                "DateOfIssued",
                "DateOfExpiration",
                "CountryCode",
                "CountryName",
                "IsResident",
                "Snils",
                "Inn"
            ]
        },
        "Contacts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "PhoneNumber": {
                        "type": "string"
                    },
                    "Email": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "Id",
                    "PhoneNumber"
                ]
            }
        },
        "EmployeeWorkplaces": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["string", "null"]
                    },
                    "Subdivision": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "type": "string"
                            },
                            "Name": {
                                "type": "string"
                            },
                            "Tenant": {
                                "type": ["string", "null"]
                            }
                        },
                        "required": [
                            "Id",
                            "Name"
                        ]
                    },
                    "JobTitle": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "type": "string"
                            },
                            "Name": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "Id",
                            "Name"
                        ]
                    },
                    "IsActive": {
                        "type": "boolean"
                    },
                    "PersonalCode": {
                        "type": "string"
                    },
                    "IsDeleted": {
                        "type": "boolean"
                    },
                    "DeleterId": {
                        "type": ["string", "null"]
                    },
                    "DeletionTime": {
                        "type": ["string", "null"]
                    },
                    "LastModificationTime": {
                        "type": ["string", "null"]
                    },
                    "LastModifierId": {
                        "type": ["string", "null"]
                    },
                    "CreationTime": {
                        "type": "string"
                    },
                    "CreatorId": {
                        "type": ["string", "null"]
                    },
                    "Id": {
                        "type": "string"
                    }
                },
                "required": [
                    "WorkBegan",
                    "Subdivision",
                    "JobTitle",
                    "IsActive",
                    "PersonalCode",
                    "IsDeleted",
                    "CreationTime",
                    "Id"
                ]
            }
        },
        "Status": {
            "type": "string"
        },
        "CreationTime": {
            "type": "string"
        },
        "AvatarUrl": {
            "type": ["string", "null"]
        }
    },
    "required": [
        "UserId",
        "Tenant",
        "FirstName",
        "LastName",
        "BirthDate",
        "Gender",
        "PersonalInfo",
        "Contacts",
        "EmployeeWorkplaces",
        "Status",
        "CreationTime"
    ]
}

certificates_id_schema_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Id": {
                "type": "string"
            },
            "ExternalId": {
                "type": ["string", "null"]
            },
            "Employee": {
                "type": "object",
                "properties": {
                    "FirstName": {
                        "type": "string"
                    },
                    "LastName": {
                        "type": "string"
                    },
                    "MiddleName": {
                        "type": ["string", "null"]
                    },
                    "BirthDate": {
                        "type": "string"
                    },
                    "Gender": {
                        "type": "string"
                    },
                    "Contacts": {
                        "type": "array"
                    },
                    "EmployeeWorkplaces": {
                        "type": "array"
                    },
                    "IsDeleted": {
                        "type": "boolean"
                    },
                    "DeleterId": {
                        "type": ["string", "null"]
                    },
                    "DeletionTime": {
                        "type": ["string", "null"]
                    },
                    "LastModificationTime": {
                        "type": "string"
                    },
                    "LastModifierId": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "CreationTime": {
                        "type": "string"
                    },
                    "CreatorId": {
                        "type": "string"
                    },
                    "Id": {
                        "type": "string"
                    }
                },
                "required": [
                    "FirstName",
                    "LastName",
                    "BirthDate",
                    "Gender",
                    "Contacts",
                    "EmployeeWorkplaces",
                    "IsDeleted",
                    "LastModificationTime",
                    "CreationTime",
                    "CreatorId",
                    "Id"
                ]
            },
            "Tenant": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Fullname": {
                        "type": "string"
                    },
                    "Shortname": {
                        "type": "string"
                    },
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "Id",
                    "Fullname",
                    "Shortname",
                    "WorkBegan"
                ]
            },
            "WorkBegan": {
                "type": "string"
            },
            "WorkEnded": {
                "type": ["string", "null"]
            },
            "CertificateType": {
                "type": "string"
            },
            "CertificateStatus": {
                "type": "string"
            },
            "RequestCertificateId": {
                "type": "string"
            }
        },
        "required": [
            "Id",
            "ExternalId",
            "Employee",
            "Tenant",
            "WorkBegan",
            "WorkEnded",
            "CertificateType",
            "CertificateStatus",
            "RequestCertificateId"
        ]
    }
}

employee_workplaces_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Subdivision": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Name": {
                        "type": "string"
                    },
                    "SubdivisionCode": {
                        "type": "integer"
                    },
                    "ParentId": {
                        "type": ["string", "null"]
                    },
                    "NumberOfSubdivisions": {
                        "type": "integer"
                    },
                    "CountEmployee": {
                        "type": "integer"
                    },
                    "SubdivisionManagers": {
                        "type": "array"
                    },
                    "TenantId": {
                        "type": "string"
                    },
                    "ExternalId": {
                        "type": ["string", "null"]
                    }
                },
                "required": [
                    "Id",
                    "Name",
                    "SubdivisionCode",
                    "NumberOfSubdivisions",
                    "CountEmployee",
                    "SubdivisionManagers",
                    "TenantId"
                ]
            },
            "PersonalCode": {
                "type": "string"
            },
            "EmployeeId": {
                "type": "string"
            },
            "WorkBegan": {
                "type": "string"
            },
            "WorkEnded": {
                "type": ["string", "null"]
            },
            "JobTitle": {
                "type": "object",
                "properties": {
                    "Name": {
                        "type": "string"
                    },
                    "IsDeleted": {
                        "type": "boolean"
                    },
                    "DeleterId": {
                        "type": ["string", "null"]
                    },
                    "DeletionTime": {
                        "type": ["string", "null"]
                    },
                    "LastModificationTime": {
                        "type": ["string", "null"]
                    },
                    "LastModifierId": {
                        "type": ["string", "null"]
                    },
                    "CreationTime": {
                        "type": "string"
                    },
                    "CreatorId": {
                        "type": ["string", "null"]
                    },
                    "Id": {
                        "type": "string"
                    }
                },
                "required": [
                    "Name",
                    "IsDeleted",
                    "CreationTime",
                    "CreatorId",
                    "Id"
                ]
            },
            "IsActive": {
                "type": "boolean"
            },
            "Employee": {
                "type": "object",
                "properties": {
                    "TenantId": {
                        "type": "string"
                    },
                    "FirstName": {
                        "type": "string"
                    },
                    "LastName": {
                        "type": "string"
                    },
                    "MiddleName": {
                        "type": ["string", "null"]
                    },
                    "BirthDate": {
                        "type": "string"
                    },
                    "Gender": {
                        "type": "string"
                    },
                    "IsDeleted": {
                        "type": "boolean"
                    },
                    "DeleterId": {
                        "type": ["string", "null"]
                    },
                    "DeletionTime": {
                        "type": ["string", "null"]
                    },
                    "LastModificationTime": {
                        "type": ["string", "null"]
                    },
                    "LastModifierId": {
                        "type": ["string", "null"]
                    },
                    "CreationTime": {
                        "type": "string"
                    },
                    "CreatorId": {
                        "type": ["string", "null"]
                    },
                    "Id": {
                        "type": "string"
                    }
                },
                "required": [
                    "TenantId",
                    "FirstName",
                    "LastName",
                    "BirthDate",
                    "Gender",
                    "IsDeleted",
                    "LastModificationTime",
                    "CreationTime",
                    "Id"
                ]
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["string", "null"]
            },
            "DeletionTime": {
                "type": ["string", "null"]
            },
            "LastModificationTime": {
                "type": ["string", "null"]
            },
            "LastModifierId": {
                "type": ["string", "null"]
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": ["string", "null"]
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "Subdivision",
            "PersonalCode",
            "EmployeeId",
            "WorkBegan",
            "JobTitle",
            "IsActive",
            "Employee",
            "IsDeleted",
            "CreationTime",
            "Id"
        ]
    }
}

employee_workplaces_by_employee_id_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Id": {
                "type": "string"
            },
            "EmployeeId": {
                "type": "string"
            },
            "PersonalCode": {
                "type": "string"
            },
            "SubdivisionName": {
                "type": "string"
            },
            "JobTitleName": {
                "type": "string"
            },
            "AccessRole": {
                "type": "string"
            },
            "WorkBegan": {
                "type": "string"
            },
            "WorkEnded": {
                "type": ["string", "null"]
            },
            "IsActive": {
                "type": "boolean"
            }
        },
        "required": [
            "Id",
            "EmployeeId",
            "PersonalCode",
            "SubdivisionName",
            "JobTitleName",
            "AccessRole",
            "WorkBegan",
            "IsActive"
        ]
    }
}

jobtitle_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {
                "type": "string"
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["string", "null"]
            },
            "DeletionTime": {
                "type": ["string", "null"]
            },
            "LastModificationTime": {
                "type": ["string", "null"]
            },
            "LastModifierId": {
                "type": ["string", "null"]
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": ["string", "null"]
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "Name",
            "IsDeleted",
            "CreationTime",
            "Id"
        ]
    }
}

subdivision_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Id": {
                "type": "string"
            },
            "Name": {
                "type": "string"
            },
            "SubdivisionCode": {
                "type": "integer"
            },
            "ParentId": {
                "type": ["null", "string"]
            },
            "ParentExternalId": {
                "type": ["null", "string"]
            },
            "NumberOfSubdivisions": {
                "type": "integer"
            },
            "CountEmployee": {
                "type": "integer"
            },
            "TenantId": {
                "type": "string"
            },
            "ExternalId": {
                "type": ["null", "string"]
            }
        },
        "required": [
            "Id",
            "Name",
            "SubdivisionCode",
            "NumberOfSubdivisions",
            "CountEmployee",
            "TenantId"
        ]
    }
}

docstorage_employee_inbox_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {
                "type": "string"
            },
            "DocumentType": {
                "type": "string"
            },
            "DocumentTypeId": {
                "type": "string"
            },
            "Status": {
                "type": "string"
            },
            "TemplateId": {
                "type": ["null", "string"]
            },
            "TemplateVersion": {
                "type": "integer"
            },
            "DateSent": {
                "type": "string"
            },
            "SigningPeriod": {
                "type": "string"
            },
            "Sender": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Employee": {
                        "type": "object",
                        "properties": {
                            "FirstName": {
                                "type": "string"
                            },
                            "LastName": {
                                "type": "string"
                            },
                            "MiddleName": {
                                "type": ["null", "string"]
                            },
                            "Gender": {
                                "type": "string"
                            },
                            "AvatarUrl": {
                                "type": ["null", "string"]
                            },
                            "IsDeleted": {
                                "type": "boolean"
                            },
                            "DeleterId": {
                                "type": ["null", "string"]
                            },
                            "DeletionTime": {
                                "type": ["null", "string"]
                            },
                            "LastModificationTime": {
                                "type": "string"
                            },
                            "LastModifierId": {
                                "type": ["null", "string"]
                            },
                            "CreationTime": {
                                "type": "string"
                            },
                            "CreatorId": {
                                "type": ["null", "string"]
                            },
                            "Id": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "FirstName",
                            "LastName",
                            "Gender",
                            "IsDeleted",
                            "LastModificationTime",
                            "CreationTime",
                            "Id"
                        ]
                    },
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["null", "string"]
                    },
                    "JobTitle": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "type": "string"
                            },
                            "Name": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "Id",
                            "Name"
                        ]
                    },
                    "Subdivision": {
                        "type": ["null", "string"]
                    },
                    "Status": {
                        "type": "string"
                    }
                },
                "required": [
                    "Id",
                    "Employee",
                    "WorkBegan",
                    "JobTitle",
                    "Status"
                ]
            },
            "Recipients": {
                "type": ["null", "string"]
            },
            "Comment": {
                "type": ["null", "string"]
            },
            "AccessAfterSigning": {
                "type": "string"
            },
            "AccessForNotActive": {
                "type": "string"
            },
            "LastSendSigningNotification": {
                "type": "string"
            },
            "NextSendSigningNotificationAllowed": {
                "type": "string"
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["null", "string"]
            },
            "DeletionTime": {
                "type": ["null", "string"]
            },
            "LastModificationTime": {
                "type": "string"
            },
            "LastModifierId": {
                "type": "string"
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": "string"
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "Name",
            "DocumentType",
            "DocumentTypeId",
            "Status",
            "TemplateVersion",
            "DateSent",
            "SigningPeriod",
            "Sender",
            "AccessAfterSigning",
            "AccessForNotActive",
            "LastSendSigningNotification",
            "NextSendSigningNotificationAllowed",
            "IsDeleted",
            "LastModificationTime",
            "LastModifierId",
            "CreationTime",
            "CreatorId",
            "Id"
        ]
    }
}

docstorage_tenant_inbox_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {
                "type": "string"
            },
            "DocumentType": {
                "type": "string"
            },
            "DocumentTypeId": {
                "type": "string"
            },
            "Status": {
                "type": "string"
            },
            "TemplateId": {
                "type": ["null", "string"]
            },
            "TemplateVersion": {
                "type": "integer"
            },
            "DateSent": {
                "type": "string"
            },
            "SigningPeriod": {
                "type": "string"
            },
            "Sender": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Employee": {
                        "type": "object",
                        "properties": {
                            "FirstName": {
                                "type": "string"
                            },
                            "LastName": {
                                "type": "string"
                            },
                            "MiddleName": {
                                "type": "string"
                            },
                            "Gender": {
                                "type": "string"
                            },
                            "AvatarUrl": {
                                "type": ["null", "string"]
                            },
                            "IsDeleted": {
                                "type": "boolean"
                            },
                            "DeleterId": {
                                "type": ["null", "string"]
                            },
                            "DeletionTime": {
                                "type": ["null", "string"]
                            },
                            "LastModificationTime": {
                                "type": ["null", "string"]
                            },
                            "LastModifierId": {
                                "type": ["null", "string"]
                            },
                            "CreationTime": {
                                "type": "string"
                            },
                            "CreatorId": {
                                "type": ["null", "string"]
                            },
                            "Id": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "FirstName",
                            "LastName",
                            "MiddleName",
                            "Gender",
                            "IsDeleted",
                            "CreationTime",
                            "Id"
                        ]
                    },
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["null", "string"]
                    },
                    "JobTitle": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "type": "string"
                            },
                            "Name": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "Id",
                            "Name"
                        ]
                    },
                    "Subdivision": {
                        "type": ["null", "string"]
                    },
                    "Status": {
                        "type": "string"
                    }
                },
                "required": [
                    "Id",
                    "Employee",
                    "WorkBegan",
                    "JobTitle",
                    "Status"
                ]
            },
            "Recipients": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Id": {
                            "type": "string"
                        },
                        "EmployeeWorkplaceId": {
                            "type": ["null", "string"]
                        },
                        "LastName": {
                            "type": ["null", "string"]
                        },
                        "FirstName": {
                            "type": ["null", "string"]
                        },
                        "MiddleName": {
                            "type": ["null", "string"]
                        },
                        "JobTitle": {
                            "type": ["null", "string"]
                        },
                        "RecipientTenant": {
                            "type": "boolean"
                        },
                        "AvatarUrl": {
                            "type": ["null", "string"]
                        }
                    },
                    "required": [
                        "Id",
                        "RecipientTenant"
                    ]
                }
            },
            "Comment": {
                "type": ["null", "string"]
            },
            "AccessAfterSigning": {
                "type": "string"
            },
            "AccessForNotActive": {
                "type": "string"
            },
            "LastSendSigningNotification": {
                "type": ["null", "string"]
            },
            "NextSendSigningNotificationAllowed": {
                "type": ["null", "string"]
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["null", "string"]
            },
            "DeletionTime": {
                "type": ["null", "string"]
            },
            "LastModificationTime": {
                "type": ["null", "string"]
            },
            "LastModifierId": {
                "type": ["null", "string"]
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": ["null", "string"]
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "Name",
            "DocumentType",
            "DocumentTypeId",
            "Status",
            "TemplateVersion",
            "DateSent",
            "SigningPeriod",
            "Sender",
            "Recipients",
            "AccessAfterSigning",
            "AccessForNotActive",
            "IsDeleted",
            "CreationTime",
            "Id"
        ]
    }
}

tenant_inbox_agreement_required_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {
                "type": "string"
            },
            "DocumentType": {
                "type": "string"
            },
            "DocumentTypeId": {
                "type": "string"
            },
            "Status": {
                "type": "string"
            },
            "TemplateId": {
                "type": ["null", "string"]
            },
            "TemplateVersion": {
                "type": "integer"
            },
            "DateSent": {
                "type": "string"
            },
            "SigningPeriod": {
                "type": "string"
            },
            "Sender": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Employee": {
                        "type": "object",
                        "properties": {
                            "FirstName": {
                                "type": "string"
                            },
                            "LastName": {
                                "type": "string"
                            },
                            "MiddleName": {
                                "type": ["null", "string"]
                            },
                            "Gender": {
                                "type": "string"
                            },
                            "AvatarUrl": {
                                "type": ["null", "string"]
                            },
                            "IsDeleted": {
                                "type": "boolean"
                            },
                            "DeleterId": {
                                "type": ["null", "string"]
                            },
                            "DeletionTime": {
                                "type": ["null", "string"]
                            },
                            "LastModificationTime": {
                                "type": ["null", "string"]
                            },
                            "LastModifierId": {
                                "type": ["null", "string"]
                            },
                            "CreationTime": {
                                "type": "string"
                            },
                            "CreatorId": {
                                "type": ["null", "string"]
                            },
                            "Id": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "FirstName",
                            "LastName",
                            "Gender",
                            "IsDeleted",
                            "CreationTime",
                            "Id"
                        ]
                    },
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["null", "string"]
                    },
                    "JobTitle": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "type": "string"
                            },
                            "Name": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "Id",
                            "Name"
                        ]
                    },
                    "Subdivision": {
                        "type": ["null", "string"]
                    },
                    "Status": {
                        "type": "string"
                    }
                },
                "required": [
                    "Id",
                    "Employee",
                    "WorkBegan",
                    "JobTitle",
                    "Status"
                ]
            },
            "Recipients": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Id": {
                            "type": "string"
                        },
                        "EmployeeWorkplaceId": {
                            "type": ["null", "string"]
                        },
                        "LastName": {
                            "type": ["null", "string"]
                        },
                        "FirstName": {
                            "type": ["null", "string"]
                        },
                        "MiddleName": {
                            "type": ["null", "string"]
                        },
                        "JobTitle": {
                            "type": ["null", "string"]
                        },
                        "RecipientTenant": {
                            "type": "boolean"
                        },
                        "AvatarUrl": {
                            "type": ["null", "string"]
                        }
                    },
                    "required": [
                        "Id",
                        "RecipientTenant"
                    ]
                }
            },
            "Comment": {
                "type": ["null", "string"]
            },
            "AccessAfterSigning": {
                "type": "string"
            },
            "AccessForNotActive": {
                "type": "string"
            },
            "LastSendSigningNotification": {
                "type": ["null", "string"]
            },
            "NextSendSigningNotificationAllowed": {
                "type": ["null", "string"]
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["null", "string"]
            },
            "DeletionTime": {
                "type": ["null", "string"]
            },
            "LastModificationTime": {
                "type": ["null", "string"]
            },
            "LastModifierId": {
                "type": ["null", "string"]
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": "string"
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "Name",
            "DocumentType",
            "DocumentTypeId",
            "Status",
            "TemplateVersion",
            "DateSent",
            "SigningPeriod",
            "Sender",
            "Recipients",
            "AccessAfterSigning",
            "AccessForNotActive",
            "IsDeleted",
            "CreationTime",
            "CreatorId",
            "Id"
        ]
    }
}

employee_sent_list: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Name": {
                "type": "string"
            },
            "DocumentType": {
                "type": "string"
            },
            "DocumentTypeId": {
                "type": "string"
            },
            "Status": {
                "type": "string"
            },
            "TemplateId": {
                "type": ["null", "string"]
            },
            "TemplateVersion": {
                "type": "integer"
            },
            "DateSent": {
                "type": "string"
            },
            "SigningPeriod": {
                "type": "string"
            },
            "Sender": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Employee": {
                        "type": "object",
                        "properties": {
                            "FirstName": {
                                "type": "string"
                            },
                            "LastName": {
                                "type": "string"
                            },
                            "MiddleName": {
                                "type": ["null", "string"]
                            },
                            "Gender": {
                                "type": "string"
                            },
                            "AvatarUrl": {
                                "type": ["null", "string"]
                            },
                            "IsDeleted": {
                                "type": "boolean"
                            },
                            "DeleterId": {
                                "type": ["null", "string"]
                            },
                            "DeletionTime": {
                                "type": ["null", "string"]
                            },
                            "LastModificationTime": {
                                "type": "string"
                            },
                            "LastModifierId": {
                                "type": ["null", "string"]
                            },
                            "CreationTime": {
                                "type": "string"
                            },
                            "CreatorId": {
                                "type": ["null", "string"]
                            },
                            "Id": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "FirstName",
                            "LastName",
                            "Gender",
                            "IsDeleted",
                            "LastModificationTime",
                            "CreationTime",
                            "Id"
                        ]
                    },
                    "WorkBegan": {
                        "type": "string"
                    },
                    "WorkEnded": {
                        "type": ["null", "string"]
                    },
                    "JobTitle": {
                        "type": ["null", "string"]
                    },
                    "Subdivision": {
                        "type": ["null", "string"]
                    },
                    "Status": {
                        "type": "string"
                    }
                },
                "required": [
                    "Id",
                    "Employee",
                    "WorkBegan",
                    "Status"
                ]
            },
            "Recipients": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Id": {
                            "type": "string"
                        },
                        "EmployeeWorkplaceId": {
                            "type": ["null", "string"]
                        },
                        "LastName": {
                            "type": ["null", "string"]
                        },
                        "FirstName": {
                            "type": ["null", "string"]
                        },
                        "MiddleName": {
                            "type": ["null", "string"]
                        },
                        "JobTitle": {
                            "type": ["null", "string"]
                        },
                        "RecipientTenant": {
                            "type": "boolean"
                        },
                        "AvatarUrl": {
                            "type": ["null", "string"]
                        }
                    },
                    "required": [
                        "Id",
                        "RecipientTenant"
                    ]
                }
            },
            "Comment": {
                "type": ["null", "string"]
            },
            "AccessAfterSigning": {
                "type": "string"
            },
            "AccessForNotActive": {
                "type": "string"
            },
            "LastSendSigningNotification": {
                "type": "string"
            },
            "NextSendSigningNotificationAllowed": {
                "type": "string"
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["null", "string"]
            },
            "DeletionTime": {
                "type": ["null", "string"]
            },
            "LastModificationTime": {
                "type": "string"
            },
            "LastModifierId": {
                "type": "string"
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": "string"
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "Name",
            "DocumentType",
            "DocumentTypeId",
            "Status",
            "TemplateVersion",
            "DateSent",
            "SigningPeriod",
            "Sender",
            "Recipients",
            "AccessAfterSigning",
            "AccessForNotActive",
            "LastSendSigningNotification",
            "NextSendSigningNotificationAllowed",
            "IsDeleted",
            "LastModificationTime",
            "LastModifierId",
            "CreationTime",
            "CreatorId",
            "Id"
        ]
    }
}

document_type_schema_v3: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "ShortName": {
                "type": "string"
            },
            "MinTrudDocumentType": {
                "type": "object",
                "properties": {
                    "Id": {
                        "type": "string"
                    },
                    "Name": {
                        "type": "string"
                    },
                    "Section": {
                        "type": "integer"
                    },
                    "Code": {
                        "type": "integer"
                    }
                },
                "required": [
                    "Id",
                    "Name",
                    "Section",
                    "Code"
                ]
            },
            "SigningPeriod": {
                "type": "string"
            },
            "SignatureTypeSender": {
                "type": "string"
            },
            "SignatureTypeReceiver": {
                "type": "string"
            },
            "SenderRole": {
                "type": "string"
            },
            "AccessAfterSigning": {
                "type": "string"
            },
            "AccessForNotActive": {
                "type": "string"
            },
            "IsDeleted": {
                "type": "boolean"
            },
            "DeleterId": {
                "type": ["null", "string"]
            },
            "DeletionTime": {
                "type": ["null", "string"]
            },
            "LastModificationTime": {
                "type": ["null", "string"]
            },
            "LastModifierId": {
                "type": ["null", "string"]
            },
            "CreationTime": {
                "type": "string"
            },
            "CreatorId": {
                "type": ["null", "string"]
            },
            "Id": {
                "type": "string"
            }
        },
        "required": [
            "ShortName",
            "MinTrudDocumentType",
            "SigningPeriod",
            "SignatureTypeSender",
            "SignatureTypeReceiver",
            "SenderRole",
            "AccessAfterSigning",
            "AccessForNotActive",
            "IsDeleted",
            "CreationTime",
            "Id"
        ]
    }
}