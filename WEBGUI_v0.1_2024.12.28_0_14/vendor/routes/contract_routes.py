from flask import Blueprint, render_template, current_app, jsonify, request, abort
from http import HTTPStatus

contract_bp = Blueprint('contract', __name__)

@contract_bp.route('/', methods=['GET'])
def get_contracts():
    try:
        # You might want to fetch contracts from a database or API
        contracts = [
            {
                'id': 1,
                'name': 'Contract A',
                'status': 'Active',
                'date': '2024-01-01'
            },
            # Add more sample contracts
        ]

        return render_template(
            'vendor/contracts.html',
            contracts=contracts,
            page_title='Contracts Dashboard'
        )
    except Exception as e:
        current_app.logger.error(f"Error in get_contracts: {str(e)}")
        return render_template('error.html', error=str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

# Add a route to get a specific contract
@contract_bp.route('/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    try:
        # Mock contract data (replace with actual database query)
        contract = {
            'id': contract_id,
            'name': f'Contract {contract_id}',
            'status': 'Active',
            'date': '2024-01-01'
        }

        # Handle API requests
        if request.headers.get('Accept') == 'application/json':
            return jsonify(contract)

        # Handle HTML requests
        return render_template(
            'vendor/contract_detail.html',
            contract=contract,
            page_title=f'Contract {contract_id} Details'
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching contract {contract_id}: {str(e)}")
        abort(404)

# Add a route to create new contract
@contract_bp.route('/', methods=['POST'])
def create_contract():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'status', 'date']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), HTTPStatus.BAD_REQUEST

        # Mock contract creation (replace with actual database insertion)
        new_contract = {
            'id': len(contracts) + 1,  # Mock ID generation
            'name': data['name'],
            'status': data['status'],
            'date': data['date']
        }

        return jsonify(new_contract), HTTPStatus.CREATED

    except Exception as e:
        current_app.logger.error(f"Error creating contract: {str(e)}")
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

# Add error handlers
@contract_bp.errorhandler(404)
def not_found_error(error):
    if request.headers.get('Accept') == 'application/json':
        return jsonify({'error': 'Contract not found'}), 404
    return render_template('404.html'), 404

@contract_bp.errorhandler(500)
def internal_error(error):
    if request.headers.get('Accept') == 'application/json':
        return jsonify({'error': 'Internal server error'}), 500
    return render_template('500.html'), 500

# Add before_request handler for logging
@contract_bp.before_request
def before_request():
    current_app.logger.info(f"Accessing: {request.endpoint} - Method: {request.method}")